#!/usr/bin/env python3
"""Регрессионные тесты маршрутизации Mihomo — проверяют РЕАЛЬНОЕ ядро, а не догадки.

Как работает: цели DIRECT / REJECT / PROXY в правилах подменяются группами
T_DIRECT / T_REJECT / T_PROXY, которые ведут в заведомо мёртвый socks5
(127.0.0.1:1). Каждое соединение падает мгновенно, а в лог ядра попадает,
какое правило и какая цель сработали. Трафик наружу не уходит (кроме DNS
для GEOIP-правил с резолвом).

Использование:
  python rules_test.py --mihomo ./mihomo --rules rules.yaml --cases cases.yaml
  python rules_test.py --mihomo ./mihomo --rules v4.yaml --compare v5.yaml --hosts-from v4.yaml

Правила по процессам (PROCESS-NAME) здесь не проверяются: тестовый клиент —
сам Python, find-process-mode выключен.
"""
import argparse, os, re, shutil, socket, struct, subprocess, sys, tempfile, threading, time
from concurrent.futures import ThreadPoolExecutor
import yaml

TARGETS = {'DIRECT': 'T_DIRECT', 'REJECT': 'T_REJECT', 'PROXY': 'T_PROXY'}
LOGIC = ('AND,', 'OR,', 'NOT,')


def retarget(rule: str) -> str:
    """Подменить цель правила на тестовую группу."""
    if rule.startswith(LOGIC):
        head, sep, tail = rule.rpartition('),')
        parts = tail.split(',')
        parts[0] = TARGETS.get(parts[0], parts[0])
        return head + sep + ','.join(parts)
    p = rule.split(',')
    i = 1 if p[0] == 'MATCH' else 2
    p[i] = TARGETS.get(p[i], p[i])
    return ','.join(p)


def build_config(rules_file, port, dns):
    src = yaml.safe_load(open(rules_file, encoding='utf-8'))
    cfg = {
        'mixed-port': port, 'log-level': 'info', 'ipv6': True,
        'find-process-mode': 'off',
        'dns': {'enable': True, 'nameserver': [dns]},
        'proxies': [{'name': 'dead', 'type': 'socks5', 'server': '127.0.0.1', 'port': 1, 'udp': True}],
        'proxy-groups': [{'name': n, 'type': 'select', 'proxies': ['dead']} for n in TARGETS.values()],
        'rules': [retarget(r) for r in src['rules']],
    }
    if 'rule-providers' in src:
        cfg['rule-providers'] = src['rule-providers']
    return cfg


CAT = {'Domain': 'DOMAIN', 'DomainSuffix': 'DOMAIN', 'DOMAIN': 'DOMAIN', 'DOMAIN-SUFFIX': 'DOMAIN',
       'DomainKeyword': 'KEYWORD', 'DOMAIN-KEYWORD': 'KEYWORD', 'DomainRegex': 'REGEX',
       'IPCIDR': 'IP', 'IPCIDR6': 'IP', 'GeoIP': 'GEOIP', 'Match': 'MATCH', 'DstPort': 'PORT',
       'AND': 'LOGIC', 'PROCESS-NAME': 'PROCESS', 'ProcessName': 'PROCESS'}

LINE = re.compile(r'\[(TCP|UDP)\] dial (\S+) \(match (.*)\) \S+ --> (\S+) ')


class Core:
    def __init__(self, mihomo, rules_file, port, dns, geodir):
        self.dir = tempfile.mkdtemp(prefix='mihomo-test-')
        for f in ('geoip.metadb', 'Country.mmdb', 'GeoIP.dat', 'GeoSite.dat', 'geoip.dat', 'geosite.dat'):
            if geodir and os.path.exists(os.path.join(geodir, f)):
                shutil.copy(os.path.join(geodir, f), self.dir)
        path = os.path.join(self.dir, 'config.yaml')
        yaml.safe_dump(build_config(rules_file, port, dns), open(path, 'w', encoding='utf-8'),
                       allow_unicode=True, sort_keys=False)
        chk = subprocess.run([mihomo, '-t', '-d', self.dir, '-f', path], capture_output=True, text=True)
        if 'test is successful' not in chk.stdout + chk.stderr:
            sys.exit(f'[{rules_file}] конфиг не прошёл mihomo -t:\n{chk.stdout}{chk.stderr}')
        self.port, self.seen, self.lock = port, {}, threading.Lock()
        self.set_cat = {}
        for name, prov in (yaml.safe_load(open(rules_file, encoding='utf-8')).get('rule-providers') or {}).items():
            b = prov.get('behavior')
            first = str(prov['payload'][0]).split(',')[0] if b == 'classical' else ''
            self.set_cat[name] = {'domain': 'DOMAIN', 'ipcidr': 'IP'}.get(b) or CAT.get(first, first)
        self.proc = subprocess.Popen([mihomo, '-d', self.dir, '-f', path], stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
        threading.Thread(target=self._reader, daemon=True).start()
        for _ in range(100):
            try:
                socket.create_connection(('127.0.0.1', port), timeout=0.2).close(); break
            except OSError:
                time.sleep(0.1)

    def _reader(self):
        for ln in self.proc.stdout:
            m = LINE.search(ln)
            if m:
                net, group, rule, dst = m.groups()
                with self.lock:
                    kind, _, rest = rule.partition('/')
                    cat = self.set_cat.get(rest, rest) if kind == 'RuleSet' else CAT.get(kind, kind)
                    self.seen.setdefault((net, dst), (group.replace('T_', ''), rule, cat))

    def probe(self, host, port, net='TCP', timeout=8.0):
        dst = f'{host}:{port}' if ':' not in host else f'[{host}]:{port}'
        try:
            if net == 'TCP':
                s = socket.create_connection(('127.0.0.1', self.port), timeout=timeout)
                s.sendall(f'CONNECT {dst} HTTP/1.1\r\nHost: {dst}\r\n\r\n'.encode())
                try: s.recv(64)
                except OSError: pass
                s.close()
            else:
                t = socket.create_connection(('127.0.0.1', self.port), timeout=timeout)
                t.sendall(b'\x05\x01\x00'); t.recv(2)
                t.sendall(b'\x05\x03\x00\x01\x00\x00\x00\x00\x00\x00')
                bport = struct.unpack('>H', t.recv(10)[8:10])[0]
                u = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                hb = host.encode()
                u.sendto(b'\x00\x00\x00\x03' + bytes([len(hb)]) + hb + struct.pack('>H', port) + b'probe',
                         ('127.0.0.1', bport))
        except OSError:
            pass
        deadline = time.time() + timeout
        key = (net, dst)
        while time.time() < deadline:
            with self.lock:
                if key in self.seen:
                    return self.seen[key]
            time.sleep(0.05)
        return ('TIMEOUT', '', '')

    def close(self):
        self.proc.kill(); self.proc.wait()
        shutil.rmtree(self.dir, ignore_errors=True)


def run_probes(core, items, workers=32):
    with ThreadPoolExecutor(workers) as ex:
        return list(ex.map(lambda it: core.probe(it['host'], it.get('port', 443), it.get('net', 'TCP').upper()), items))


def hosts_from(rules_file):
    """Все домены из правил и провайдеров: сам домен + поддомен (проверка suffix/exact)."""
    src = yaml.safe_load(open(rules_file, encoding='utf-8'))
    doms = []
    for r in src['rules']:
        p = r.split(',')
        if p[0] in ('DOMAIN', 'DOMAIN-SUFFIX'):
            doms.append(p[1])
    for prov in (src.get('rule-providers') or {}).values():
        if prov.get('behavior') == 'domain':
            doms += [d[2:] if d.startswith('+.') else d for d in prov['payload']]
    out = []
    for d in dict.fromkeys(doms):
        if not d.isascii():
            continue
        out += [{'host': d}, {'host': 'zz-test.' + d}]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mihomo', required=True)
    ap.add_argument('--rules', required=True)
    ap.add_argument('--cases')
    ap.add_argument('--compare')
    ap.add_argument('--hosts-from')
    ap.add_argument('--dns', default='8.8.8.8')
    ap.add_argument('--geodir', default='.')
    a = ap.parse_args()

    core = Core(a.mihomo, a.rules, 17890, a.dns, a.geodir)
    failed = 0
    try:
        if a.cases:
            cases = yaml.safe_load(open(a.cases, encoding='utf-8'))
            res = run_probes(core, cases)
            for c, (got, rule, _cat) in zip(cases, res):
                ok = got == c['expect']
                failed += not ok
                mark = 'OK  ' if ok else 'FAIL'
                print(f"{mark} {c.get('net','tcp').upper():3} {c['host']}:{c.get('port',443):<5} "
                      f"→ {got:<7} ({rule})  {'' if ok else 'ожидалось ' + c['expect']}  {c.get('why','')}")
            print(f'\nИтого: {len(cases) - failed}/{len(cases)} прошло')
        if a.compare:
            items = hosts_from(a.hosts_from or a.rules)
            base = run_probes(core, items)
            core.close()
            core = Core(a.mihomo, a.compare, 17891, a.dns, a.geodir)
            new = run_probes(core, items)
            # сравниваем цель И класс сработавшего правила: DIRECT-через-GEOIP ≠ DIRECT-через-список
            diff = [(it['host'], f'{b[0]}/{b[2]}', f'{n[0]}/{n[2]}') for it, b, n in zip(items, base, new)
                    if (b[0], b[2]) != (n[0], n[2])]
            timeouts = sum(1 for b, n in zip(base, new) if 'TIMEOUT' in (b[0], n[0]))
            print(f'Сравнение {a.rules} ↔ {a.compare}: {len(items)} хостов, расхождений: {len(diff)}, таймаутов: {timeouts}')
            for d in diff[:50]:
                print('  DIFF', *d)
            failed += len(diff)
    finally:
        core.close()
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
