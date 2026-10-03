# Development and reproducible build

## Requirements

- Python 3.8+
- Node.js (only for JavaScript syntax validation)
- No npm packages are required
- No Internet access is required for the local build

## Source layout

```text
src/index.template.html  HTML shell with inline placeholders
src/styles.css           release CSS
src/emulator.js          release JavaScript
```

## Build

```bash
python3 tools/build.py
```

The command regenerates:

```text
index.html
dist/WonderSwan_Mobile_Emulator_v1.6.3_CaptureBundleHotkeys.html
```

The v1.6.3 repository is configured for reproducibility: those generated files must have SHA-256:

```text
ee56094b09f97796be120b037455fdf397e42bdf1029190518afa64b8f046c62
```

## Check without overwriting

```bash
python3 tools/build.py --check
```

## Validation

```bash
python3 tools/validate.py
```

The validator checks build reproducibility, release hash, JavaScript syntax when Node is available, required hotkey assignments, and the offline/network audit.

## Windows

```bat
build.bat
```

## macOS

```bash
chmod +x build.command
./build.command
```

## Editing rule

Edit the files in `src/`, not the generated `index.html`. Rebuild before committing.

When emulation code changes, create a new version rather than silently changing the v1.6.3 hash.
