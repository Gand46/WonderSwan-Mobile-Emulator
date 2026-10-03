#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'index.html'
JS = ROOT / 'src' / 'emulator.js'
EXPECTED_SHA256 = 'ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62'


def fail(msg: str) -> None:
    print('FAIL:', msg)
    raise SystemExit(1)


def require(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)
    print('PASS:', msg)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'build.py'), '--check'], check=True)

    require(HTML.exists(), 'index.html exists')
    data = HTML.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    require(digest == EXPECTED_SHA256, f'release SHA-256 is {EXPECTED_SHA256}')

    text = data.decode('utf-8')
    js = JS.read_text(encoding='utf-8')

    # Offline/no-network release audit.
    require('connect-src \'none\'' in text, "CSP connect-src is 'none'")
    require('http://' not in text and 'https://' not in text, 'release contains no HTTP/HTTPS URLs')
    require('fetch(' not in js, 'release JavaScript contains no fetch()')
    require('XMLHttpRequest' not in js, 'release JavaScript contains no XMLHttpRequest')
    require('WebSocket' not in js, 'release JavaScript contains no WebSocket')

    # Expected hotkeys introduced by v1.6.3.
    compact = js.replace(' ', '')
    expected_bindings = [
        ("ArrowUp:'xu'", 'Arrow Up -> X1 binding'),
        ("ArrowRight:'xr'", 'Arrow Right -> X2 binding'),
        ("ArrowDown:'xd'", 'Arrow Down -> X3 binding'),
        ("ArrowLeft:'xl'", 'Arrow Left -> X4 binding'),
        ("w:'yu'", 'W -> Y1 binding'),
        ("d:'yr'", 'D -> Y2 binding'),
        ("s:'yd'", 'S -> Y3 binding'),
        ("a:'yl'", 'A-key -> Y4 binding'),
        ("z:'a'", 'Z -> WonderSwan A binding'),
        ("x:'b'", 'X -> WonderSwan B binding'),
        ("c:'start'", 'C -> START binding'),
    ]
    for needle, label in expected_bindings:
        require(needle in compact, label)

    require('hot={p:()=>takeScreenshot(),g:()=>toggleGifCapture(),m:()=>capturePngMssZip()}' in compact, 'P/G/M capture hotkey map')
    require('capturePngMssZip' in js, 'PNG + MSS capture function present')
    require('buildMesenMss' in js, 'Mesen MSS export bridge present')

    node = shutil.which('node')
    if node:
        subprocess.run([node, '--check', str(JS)], check=True)
        print('PASS: node --check src/emulator.js')
    else:
        print('SKIP: Node.js not available; JavaScript syntax check not executed')

    required = [
        'README.md', 'LICENSE', 'CHANGELOG.md', 'THIRD_PARTY_NOTICES.md',
        'docs/USER_GUIDE.md', 'docs/CONTROLS.md', 'docs/MESEN_COMPATIBILITY.md',
        'docs/BIOS_AND_SAVES.md', 'docs/ARCHITECTURE.md', 'docs/DEVELOPMENT.md',
        'docs/VALIDATION.md', 'docs/KNOWN_LIMITATIONS.md',
        'validation/v1.6.3_VALIDATION.txt', 'SHA256SUMS.txt',
    ]
    for rel in required:
        require((ROOT / rel).exists(), f'{rel} exists')

    print('\nAll repository validation checks passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
