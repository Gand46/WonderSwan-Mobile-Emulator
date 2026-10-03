# BIOS, EEPROM, and save files

## No firmware is included

This project does not distribute WonderSwan or WonderSwan Color BIOS/EEPROM files.

The user may install legally obtained firmware locally in the browser. Firmware is persisted through IndexedDB and never needs to leave the device.

## Firmware ZIP layout

### WonderSwan

```text
firmware.zip
├── boot.rom                 # 4,096 bytes
└── internal_eeprom.ws       # 128 bytes
```

### WonderSwan Color

```text
firmware.zip
├── boot.rom                 # 8,192 bytes
└── internal_eeprom.wsc      # 2,048 bytes
```

The importer validates the expected file sizes.

## Save files

The emulator distinguishes three persistent storage types:

- `.sav` — cartridge SRAM;
- `.eeprom` — cartridge EEPROM;
- `.ieeprom` — internal console EEPROM.

The currently loaded cartridge determines whether SRAM or cartridge EEPROM is valid.

## Backup recommendation

Browser storage is convenient but should not be treated as the only backup. Export important save data before:

- clearing browser/site data;
- changing browsers;
- resetting the device;
- reinstalling the browser;
- moving to another phone/computer.
