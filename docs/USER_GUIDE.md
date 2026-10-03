# User guide

## Opening the emulator

The emulator is a self-contained HTML application. You can open `index.html` directly, but mobile browsers may apply stricter storage rules to `file://` pages. For reliable local persistence, serving the directory through localhost is recommended.

```bash
python3 -m http.server 8080
```

Open `http://127.0.0.1:8080/` in the browser.

## Loading a game

1. Press **ROM**.
2. Select a `.ws` or `.wsc` file.
3. Press **Play** if auto-resume is not enabled.

The emulator can keep a local recent-ROM library in IndexedDB. This does not upload the ROM anywhere.

## Portrait and landscape

The layout selector supports:

- Auto
- Portrait
- Landscape

Portrait uses a compact lower control area. Landscape follows a WonderSwan-inspired control arrangement with Y above X on the left and START/A/B on the opposite side.

## Fast Forward

The dedicated Fast Forward button is a toggle:

1. Tap once to enable 3× speed.
2. It remains active without holding the button.
3. Tap again to disable it.
4. The emulator restores the speed that was active before Fast Forward was enabled.

## Quick states

Four local quick-state slots are available. These are the emulator's own local quick-state format and are distinct from Mesen `.mss` files.

Mesen state import/export is available separately in the compatibility section.

## Screenshots

Use **PNG** or press `P` to download a lossless screenshot of the native game framebuffer.

## Animated GIF

Use **GIF** or press `G`:

- first press: start recording;
- second press: stop and encode;
- capture rate: 15 FPS;
- maximum duration: 30 seconds;
- only the game framebuffer is recorded;
- touch controls and UI overlays are not included.

## PNG + MSS evidence bundle

Use **PNG + MSS** or press `M` to create a synchronized evidence package. The emulator temporarily stops execution while both artifacts are generated.

The resulting ZIP contains one PNG and one Mesen `.mss` state from the same frame.

## Battery saves

Depending on the cartridge, the emulator supports:

- SRAM `.sav`;
- cartridge `.eeprom`;
- internal console `.ieeprom`.

Always keep exported backups before clearing browser storage.
