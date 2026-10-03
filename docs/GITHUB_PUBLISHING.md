# GitHub publishing guide

Recommended repository name:

```text
WonderSwan-Mobile-Emulator
```

Recommended description:

```text
Offline mobile-first WonderSwan / WonderSwan Color emulator in a single HTML file, with touch controls, Mesen save-state compatibility, GIF/PNG capture and synchronized PNG+MSS QA bundles.
```

## Option A — GitHub CLI

From this repository directory:

```bash
git init
git add .
git commit -m "Release v1.6.3 - Capture Bundle & Hotkeys"
git branch -M main
gh repo create WonderSwan-Mobile-Emulator --public --source=. --remote=origin --push
```

If you prefer to review it privately first, replace `--public` with `--private`.

## Option B — create an empty repository in the GitHub UI

Create an empty repository named `WonderSwan-Mobile-Emulator` without adding a generated README/license/gitignore, then run:

```bash
git init
git add .
git commit -m "Release v1.6.3 - Capture Bundle & Hotkeys"
git branch -M main
git remote add origin https://github.com/<YOUR_USER>/WonderSwan-Mobile-Emulator.git
git push -u origin main
```

## GitHub Pages

Because `index.html` is a complete self-contained emulator, the repository can also be published with GitHub Pages.

In GitHub:

```text
Settings → Pages → Build and deployment → Deploy from a branch
Branch: main
Folder: /
```

The release itself does not need network access after the page is loaded.

## Release tag

Recommended tag:

```text
v1.6.3
```

Recommended release title:

```text
WonderSwan Mobile Emulator v1.6.3 — Capture Bundle & Hotkeys
```

Use `.github/RELEASE_v1.6.3.md` as the release body.
