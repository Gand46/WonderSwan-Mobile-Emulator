# Changelog

## v1.6.3 — Capture Bundle & Hotkeys

### Added

- Synchronized **PNG + Mesen `.mss` ZIP** capture.
- Keyboard gameplay mapping:
  - Arrow keys → X1-X4.
  - WASD → Y1-Y4.
  - Z → A.
  - X → B.
  - C → START.
- Capture hotkeys:
  - `P` → PNG.
  - `G` → start/stop GIF.
  - `M` → PNG + MSS ZIP.
- Visible hotkey badges in the UI.
- Dedicated keyboard/hotkey reference card.

### Preserved

- v1.6.2 GIF capture.
- v1.6.1 persistent Fast Forward toggle.
- v1.6.0 Mesen state interoperability and user firmware support.
- v1.5 mobile-first UI layout.
- v1.4 graphics-fidelity PPU work.

### Validation summary

- JavaScript syntax: PASS.
- Gameplay keyboard matrix: 11/11 press/release PASS.
- `P`, `G`, `M` hotkeys: PASS.
- PNG + MSS ZIP structure: PASS.
- Mesen state signature/header: PASS.
- Landscape overflow: 0.
- Emulation core byte-equivalent to v1.6.2: YES.
- Offline audit: PASS.

See `validation/v1.6.3_VALIDATION.txt` for the preserved report.

## v1.6.2 — GIF Capture

- Added fully offline animated GIF capture.
- 15 FPS capture rate.
- 30-second automatic safety limit.
- Native framebuffer capture without UI overlays.
- Rotation-aware 224×144 / 144×224 export.

## v1.6.1 — Fast Forward Toggle

- Added a dedicated persistent 3× Fast Forward control.
- Restores the user's previous speed when disabled.

## v1.6.0 — Mesen State Compatibility

- Added Mesen 2.1.1 `.mss` import/export bridge.
- Added `.sav`, `.eeprom`, and `.ieeprom` interoperability.
- Added user-supplied WonderSwan/WonderSwan Color firmware storage.

## v1.5.0 — Mobile UI Polish

- Refined portrait and landscape ergonomics.
- Landscape layout places Y above X on the left and START/A/B on the right.

## v1.4.0 — Graphics Fidelity

- Improved PPU scanline behavior, latching, windows, sprite handling, and monochrome initialization.
- Added additional pixel-comparison validation against Mesen.
