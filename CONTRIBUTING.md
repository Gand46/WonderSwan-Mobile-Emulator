# Contributing

Contributions are welcome when they preserve the project's offline, reproducible, mobile-first design.

## Before submitting a change

1. Rebuild the single-file release with `python3 tools/build.py`.
2. Run `python3 tools/validate.py`.
3. Test portrait and landscape layouts when UI code changes.
4. Test at least one WonderSwan and one WonderSwan Color case when emulation code changes.
5. Re-run Mesen interoperability tests when state serialization, memory, CPU, PPU, APU, EEPROM, DMA, IRQ, or mapper state changes.
6. Do not commit ROMs, BIOS images, SRAM/EEPROM files, save states from commercial games, or other copyrighted game data.

## Pull requests

Please describe:

- the problem being solved;
- files/components changed;
- validation performed;
- regressions checked;
- any known limitations that remain.

For graphics or UI changes, include before/after screenshots when possible.
