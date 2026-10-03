# Architecture

## Distribution model

The production artifact is intentionally a single offline HTML file. CSS and JavaScript are inlined so the emulator can be copied to a phone and used without a web server dependency or package manager.

For code review and maintenance, the repository splits that file into:

```text
src/index.template.html
src/styles.css
src/emulator.js
```

`tools/build.py` reconstructs the exact release HTML.

## Main emulation components

The JavaScript core contains dedicated classes for:

- `V30CPU` — NEC V30MZ-compatible CPU implementation;
- `WSBus` — memory, ports, cartridge mapping, and system state;
- `WSPPU` — WonderSwan display pipeline;
- `WSAudio` — WonderSwan audio channels and sample generation;
- `WSEEPROM` — internal/cartridge EEPROM behavior;
- `WSRTC` — real-time clock state;
- `WSComm` — communications state;
- `WSCore` — system orchestration, timing, frame execution, inputs, and state integration.

## Graphics pipeline

The current line of development includes scanline-oriented PPU behavior, latched background/window state, sprite handling and limits, tile/palette modes, and WonderSwan monochrome initialization behavior developed and regression-tested against reference behavior.

## Persistence

IndexedDB is used for local persistence of:

- recent ROMs;
- last ROM;
- settings;
- quick states;
- firmware;
- save data.

Exports are generated locally through browser Blob/download APIs.

## Capture pipeline

### PNG

The current native framebuffer is converted to a PNG through the browser canvas.

### GIF

GIF capture uses an internal GIF89a encoder and an internal RGB332 palette. No external encoder is downloaded.

### PNG + MSS

The core is paused while the native screenshot and Mesen state are generated. An internal STORE-mode ZIP writer packages both artifacts.

## Mesen state bridge

The Mesen bridge implements the relevant MSS header and WonderSwan serializer records in JavaScript. It is deliberately isolated from normal quick-state storage so native browser quick states and interoperable `.mss` files remain separate concepts.
