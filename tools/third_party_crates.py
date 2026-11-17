"""Rewrite the crate tables at the end of THIRD_PARTY_NOTICES.md from Cargo.lock.

    python tools/third_party_crates.py           # rewrite the tables
    python tools/third_party_crates.py --check   # exit 1 when they are out of date

One table per released binary (Windows exe, Linux binary): every crate `cargo tree -e normal` links for that target,
grouped by the licence expression its Cargo.toml declares. Needs cargo; standard library only.
"""
import argparse
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
NOTICES = HERE / 'THIRD_PARTY_NOTICES.md'
MARKER = '<!-- crate tables: tools/third_party_crates.py -->'
TARGETS = [('Windows: `totk-config.exe`', 'x86_64-pc-windows-msvc'),
           ('Linux: `totk-config` in `totk-config-linux-x86_64.tar.gz`', 'x86_64-unknown-linux-gnu')]


def crates(target):
    out = subprocess.run(['cargo', 'tree', '-e', 'normal', '--locked', '--target', target, '--prefix', 'none',
                          '-f', '{p}|{l}'], cwd=HERE, capture_output=True, text=True, check=True).stdout
    by_licence = defaultdict(set)
    for line in out.splitlines():
        line = line.replace(' (*)', '').replace(' (proc-macro)', '').strip()
        if '|' not in line:
            continue
        pkg, licence = line.split('|', 1)
        name, version = pkg.split()[:2]
        if name != 'totk-config':
            by_licence[licence or 'unknown'].add(f'{name} {version}')
    return by_licence


def tables():
    parts = [MARKER, '']
    for title, target in TARGETS:
        parts += [f'### {title}', '', '| Licence | Crates |', '| --- | --- |']
        for licence, names in sorted(crates(target).items()):
            parts.append(f'| {licence} | {", ".join(sorted(names))} |')
        parts.append('')
    return '\n'.join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    text = NOTICES.read_text(encoding='utf-8')
    head = text.split(MARKER)[0]
    new = head + tables()
    if args.check:
        if new != text:
            print('THIRD_PARTY_NOTICES.md crate tables are out of date: run python tools/third_party_crates.py')
            return 1
        return 0
    NOTICES.write_text(new, encoding='utf-8', newline='\n')
    print('wrote the crate tables of THIRD_PARTY_NOTICES.md')
    return 0


if __name__ == '__main__':
    sys.exit(main())
