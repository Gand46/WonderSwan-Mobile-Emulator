# Validation

## Preserved v1.6.3 acceptance results

The release validation recorded:

- JavaScript syntax: PASS.
- Keyboard gameplay matrix: 11/11 press + release PASS.
- Arrow keys → X1-X4: PASS.
- WASD → Y1-Y4: PASS.
- Z → A: PASS.
- X → B: PASS.
- C → START: PASS.
- `P` PNG hotkey: PASS.
- `G` GIF toggle hotkey: PASS.
- `M` PNG + MSS ZIP hotkey: PASS.
- ZIP integrity: PASS.
- PNG signature: PASS.
- MSS signature: PASS.
- Mesen emulator version field: 2.1.1.
- Mesen state format: 4.
- Console type: WonderSwan.
- MSS framebuffer: 224×144.
- Serializer keys in the acceptance state: 264.
- PNG/MSS frame synchronization: PASS.
- Landscape overflow: 0.
- Emulation core preserved from v1.6.2: YES.
- Offline audit: PASS.

See `validation/v1.6.3_VALIDATION.txt` for the original report.

## Reproducible release hash

```text
ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62
```

## What this does not prove

These checks do not establish perfect compatibility with every WonderSwan title or cycle-exact equivalence with hardware/Mesen. They document the tested release surface and should be extended whenever the emulation core changes.
