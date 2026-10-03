# WonderSwan Mobile Emulator

A single-file, offline **WonderSwan / WonderSwan Color emulator for modern mobile browsers**, with a mobile-first UI, touch controls, local ROM library, quick states, Mesen save-state interoperability, screenshots, animated GIF capture, and synchronized PNG + Mesen `.mss` evidence bundles.

Current release: **v1.6.3 – Capture Bundle & Hotkeys**

> This repository does **not** include commercial ROMs, BIOS files, SRAM/EEPROM files, save states, or copyrighted game assets. Users must provide their own legally obtained files.

## Highlights

- Runs as a **single offline HTML file** with no runtime CDN or network dependency.
- Mobile-first portrait and landscape layouts designed around WonderSwan ergonomics.
- Full touch layout for `X1-X4`, `Y1-Y4`, `A`, `B`, and `START`.
- Dedicated persistent **Fast Forward 3×** toggle.
- Four local quick-state slots plus automatic state persistence.
- Local ROM library and last-ROM auto-load via IndexedDB.
- Import/export of Mesen 2.1.1 WonderSwan `.mss` save states.
- SRAM `.sav`, cartridge `.eeprom`, and internal `.ieeprom` support.
- Optional user-supplied WonderSwan / WonderSwan Color BIOS + internal EEPROM packages.
- PNG screenshot capture.
- Offline animated GIF capture at 15 FPS, up to 30 seconds.
- **PNG + Mesen MSS** synchronized capture bundle in one ZIP.
- Bluetooth/USB Gamepad API support.
- Fullscreen, orientation control, display filters, HUD, haptics, and wake-lock support where available.

## Quick start

### Easiest method

1. Download `index.html` or the versioned file from `dist/`.
2. Open it in a modern Chromium-based browser.
3. Press **ROM** and select a `.ws` or `.wsc` file.
4. The selected ROM can be stored locally in the browser so subsequent launches can auto-load it.
5. Press **Play**.

For Android, serving the file from a local HTTP server is recommended when browser storage behavior under `file://` is restrictive.

Example:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://127.0.0.1:8080/
```

No Internet access is required by the emulator after the repository has been obtained.

## Keyboard controls

| WonderSwan control | Keyboard |
|---|---|
| X1 | Arrow Up |
| X2 | Arrow Right |
| X3 | Arrow Down |
| X4 | Arrow Left |
| Y1 | W |
| Y2 | D |
| Y3 | S |
| Y4 | A |
| A | Z |
| B | X |
| START | C |

### Capture hotkeys

| Function | Hotkey |
|---|---|
| PNG screenshot | `P` |
| Start/stop animated GIF | `G` |
| PNG + Mesen MSS ZIP | `M` |

The capture hotkeys are intentionally separate from the gameplay mapping.

See [docs/CONTROLS.md](docs/CONTROLS.md) for the complete input reference.

## Synchronized PNG + MSS capture

v1.6.3 adds an evidence-oriented capture mode. The emulator pauses the core for the duration of the capture operation, then creates:

```text
<Game>_<frame>_PNG_MSS.zip
├── <Game>_<frame>.png
└── <Game>_<frame>.mss
```

The PNG and Mesen state are generated from the **same emulation instant**. This is useful for translation QA, regression reports, reproducible bug reports, and visual evidence.

## Mesen compatibility

The emulator includes a bridge for **Mesen 2.1.1 WonderSwan save states (`.mss`, format 4)**.

Validated functionality includes:

- Mesen `.mss` → this emulator.
- This emulator → Mesen `.mss`.
- WonderSwan serializer key/size compatibility for the validated state universe.
- SRAM transfer through `.sav`.
- Cartridge EEPROM transfer through `.eeprom`.
- Internal console EEPROM transfer through `.ieeprom`.

Save-state compatibility is version-sensitive. Future Mesen state-format changes are not automatically guaranteed.

See [docs/MESEN_COMPATIBILITY.md](docs/MESEN_COMPATIBILITY.md).

## BIOS support

BIOS files are **not distributed** with this repository.

The emulator can store user-supplied firmware locally in IndexedDB. The supported ZIP layout is documented in [docs/BIOS_AND_SAVES.md](docs/BIOS_AND_SAVES.md).

Validated package sizes:

| Model | `boot.rom` | Internal EEPROM |
|---|---:|---:|
| WonderSwan | 4,096 bytes | 128 bytes |
| WonderSwan Color | 8,192 bytes | 2,048 bytes |

## Build from source

The distributed emulator is intentionally a single HTML file, but the repository also provides a review-friendly split source tree:

```text
src/
├── index.template.html
├── styles.css
└── emulator.js
```

Rebuild the exact v1.6.3 release with:

```bash
python3 tools/build.py
```

Windows:

```bat
build.bat
```

macOS:

```bash
./build.command
```

The build script must reproduce the release byte-for-byte. See [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Validation

Run:

```bash
python3 tools/validate.py
```

The validation checks include:

- exact reproducible build;
- JavaScript syntax;
- expected hotkey bindings;
- offline/no-network audit;
- versioned release hash;
- required project files.

The original v1.6.3 validation report is preserved in [`validation/v1.6.3_VALIDATION.txt`](validation/v1.6.3_VALIDATION.txt).

Expected release SHA-256:

```text
ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62
```

## Architecture

The emulator is implemented in JavaScript and includes dedicated components for the NEC V30MZ CPU, bus/memory mapping, PPU, APU, EEPROM, RTC, communications, and the higher-level WonderSwan core.

The v1.4 graphics-fidelity work introduced scanline latching, sprite-line limits, sprite-table behavior, WonderSwan monochrome post-BIOS palette behavior, and other PPU corrections validated against Mesen in the project test corpus.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/KNOWN_LIMITATIONS.md](docs/KNOWN_LIMITATIONS.md).

## Offline / privacy model

The release HTML uses a restrictive Content Security Policy and does not require remote services for emulation. ROMs, firmware, saves, states, captures, and preferences remain on the user's device unless the user explicitly exports a file.

The v1.6.3 validation reported:

```text
HTTP/HTTPS URLs: 0
external scripts: 0
fetch(): 0
XMLHttpRequest: 0
WebSocket: 0
CSP connect-src: none
```

## Legal and firmware notice

- No commercial ROM is included.
- No WonderSwan BIOS is included.
- No Nintendo/Bandai/Namco/Capcom/etc. game asset is required by the repository itself.
- WonderSwan and WonderSwan Color are trademarks of their respective owners.
- This project is not affiliated with or endorsed by Bandai.

## Mesen acknowledgement

Mesen 2 was used as an important behavioral and save-state compatibility reference during development and validation. Mesen 2 is distributed under the GNU GPL v3.

- Project: `SourMesen/Mesen2`
- License: GPL-3.0

Because this project includes work developed against GPL-licensed Mesen implementation details and compatibility structures, this repository is distributed under **GPL-3.0**. See [`LICENSE`](LICENSE) and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Project documentation

- [Controls and hotkeys](docs/CONTROLS.md)
- [User guide](docs/USER_GUIDE.md)
- [Mesen compatibility](docs/MESEN_COMPATIBILITY.md)
- [BIOS and save files](docs/BIOS_AND_SAVES.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Development and reproducible build](docs/DEVELOPMENT.md)
- [Validation](docs/VALIDATION.md)
- [Known limitations](docs/KNOWN_LIMITATIONS.md)
- [GitHub publishing guide](docs/GITHUB_PUBLISHING.md)
- [Release checklist](RELEASE_CHECKLIST.md)
- [Changelog](CHANGELOG.md)

## Version

**WonderSwan Mobile Emulator v1.6.3 – Capture Bundle & Hotkeys**  
Release source hash: `ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62`
