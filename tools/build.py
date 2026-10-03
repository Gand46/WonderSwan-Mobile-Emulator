#!/usr/bin/env python3
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'src' / 'index.template.html'
CSS = ROOT / 'src' / 'styles.css'
JS = ROOT / 'src' / 'emulator.js'
OUT = ROOT / 'index.html'
VERSIONED = ROOT / 'dist' / 'WonderSwan_Mobile_Emulator_v1.6.3_CaptureBundleHotkeys.html'
EXPECTED_SHA256 = 'ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62'


def build_bytes() -> bytes:
    template = TEMPLATE.read_text(encoding='utf-8')
    css = CSS.read_text(encoding='utf-8')
    js = JS.read_text(encoding='utf-8')
    if template.count('{{INLINE_CSS}}') != 1 or template.count('{{INLINE_JS}}') != 1:
        raise SystemExit('Template placeholders are missing or duplicated.')
    text = template.replace('{{INLINE_CSS}}', css).replace('{{INLINE_JS}}', js)
    return text.encode('utf-8')


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description='Build the single-file WonderSwan Mobile Emulator release.')
    parser.add_argument('--check', action='store_true', help='Check reproducibility without overwriting files.')
    args = parser.parse_args()

    data = build_bytes()
    digest = sha256(data)

    if args.check:
        ok = True
        for path in (OUT, VERSIONED):
            if not path.exists() or path.read_bytes() != data:
                print(f'FAIL: {path.relative_to(ROOT)} does not match rebuilt output')
                ok = False
            else:
                print(f'PASS: {path.relative_to(ROOT)} matches rebuilt output')
        if digest != EXPECTED_SHA256:
            print(f'FAIL: rebuilt SHA-256 {digest} != expected {EXPECTED_SHA256}')
            ok = False
        else:
            print(f'PASS: SHA-256 {digest}')
        return 0 if ok else 1

    OUT.write_bytes(data)
    VERSIONED.parent.mkdir(parents=True, exist_ok=True)
    VERSIONED.write_bytes(data)
    print(f'Built {OUT.relative_to(ROOT)}')
    print(f'Built {VERSIONED.relative_to(ROOT)}')
    print(f'SHA-256 {digest}')
    if digest != EXPECTED_SHA256:
        print('WARNING: output differs from the preserved v1.6.3 release hash; bump the version before release.')
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
