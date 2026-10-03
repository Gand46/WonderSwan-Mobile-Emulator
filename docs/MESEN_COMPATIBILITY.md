# Mesen compatibility

## Target

The compatibility bridge in this release targets **Mesen 2.1.1** WonderSwan save states using Mesen save-state **format version 4**.

## Supported directions

### Mesen → WonderSwan Mobile Emulator

A `.mss` state can be imported while the matching ROM is loaded. The importer parses the MSS header, framebuffer data, and Mesen key/value serializer records, then maps the supported WonderSwan state into the JavaScript core.

### WonderSwan Mobile Emulator → Mesen

The emulator can export a `.mss` file using the expected Mesen header and serializer layout. Validation for the project test corpus confirmed matching serializer key names/sizes and successful loading in Mesen 2.1.1.

## Synchronized PNG + MSS

v1.6.3 can create a ZIP with a PNG screenshot and `.mss` state from the same emulation instant. This is the preferred evidence format for reproducible visual reports.

## Battery files

| Data | Extension | Notes |
|---|---|---|
| Cartridge SRAM | `.sav` | Raw battery-backed SRAM bytes |
| Cartridge EEPROM | `.eeprom` | Raw cartridge EEPROM bytes |
| Internal console EEPROM | `.ieeprom` | Raw console EEPROM bytes |

## Firmware dependency

A Mesen state captured while the boot ROM is still mapped requires the matching firmware to be installed locally before the state can continue correctly.

No BIOS or EEPROM firmware is distributed by this repository.

## Compatibility boundaries

The bridge is not a promise of compatibility with every future Mesen version. Save-state internals can change. Revalidate interoperability whenever:

- Mesen changes the file-format version;
- CPU serialization changes;
- PPU/APU/DMA/IRQ state changes;
- mapper or EEPROM serialization changes;
- the emulator's own state model changes.
