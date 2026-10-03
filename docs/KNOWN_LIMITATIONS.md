# Known limitations

The project should be described as a high-compatibility mobile WonderSwan emulator under active development, not as a cycle-exact replacement for Mesen or original hardware.

Current known boundaries include:

- V30MZ timing is calibrated but not demonstrated as fully cycle-exact for the complete software library.
- Some animation checkpoints can be separated from Mesen by a small number of frames even when aligned framebuffer output is identical.
- HyperVoice coverage is not yet considered complete.
- SwanCrystal-specific behavior has less validation coverage than standard WonderSwan / WonderSwan Color paths.
- Mesen save-state interoperability is explicitly targeted at Mesen 2.1.1 / MSS format 4; future Mesen formats require revalidation.
- Browser APIs vary by Android/browser version. Orientation locking, wake lock, vibration, and Gamepad API behavior may be unavailable or require fullscreen/user interaction.
- GIF output uses a 256-color RGB332 palette, so animated captures can show color banding compared with lossless PNG screenshots.

Please report title-specific graphical, timing, save/load, audio, or input regressions with a legal reproducible test case when possible.
