# Aetherfall — The Lost Chronicle

**Chapter I: The Bell of Ashwood** is an original browser-first fantasy RPG vertical slice using Babylon.js 7.54.3 and KayKit's stylized 3D assets.

## Install in the existing repository
1. Preserve the current `3d/index.html` by renaming it `3d/wildwood.html` if you want to retain the demo.
2. Extract this ZIP and copy its **3d/** contents into the existing **3d/** folder. Do not replace the repository root. The archive does not overwrite the original importer, CLAUDE.md, or README.md.
3. Commit the new files. In GitHub Settings → Pages, deploy from main / (root), if not already configured.
4. Open `https://fireslash92.github.io/claude-2d-game-studio/3d/`. This is the intended URL, not a confirmed live deployment.

No Blender, Unity, Unreal, npm install, or desktop application is required to play. The initial version loads pinned remote model URLs and engine scripts over HTTPS; it requires network access and WebGL. The game can also use locally vendored files.

## Controls and quest
- Touch: left joystick, hold Run, drag the canvas to orbit, Interact for NPCs/enemies/chest, View to rotate 90 degrees.
- Keyboard: WASD or arrows, Shift to run, E to interact, I to open inventory.
- Talk to Elder Mira, defeat the forest sentinel, follow the road to Silverkeep, enter the crypt, defeat the guardian, open the chest, return to Mira.
- Combat: Strike (20), Radiant cut (34, two charges), Guard (reduces incoming damage and restores a charge), Potion (heals 45). Defeat returns you to Ashwood and deducts five gold.
- The game automatically saves quest progress, inventory and position in localStorage. New game resets only the Aetherfall save.

## Asset pipeline
All 23 selected models use exact, pinned KayKit repository paths in `asset-manifest.json`. In a network-enabled cloud environment:

```sh
python3 3d/import_assets.py
python3 3d/vendor_selected.py
```

The first command imports the full packs with your existing script. The second vendors only the selected GLB/glTF files and dependencies, preserves original license notices and generates `assets/selected/inspection.json`. It also vendors the pinned Babylon.js engine. The game automatically prefers local assets when READY manifests are present. Commit only the selected assets, dependencies, license files and engine vendor folder for an internet-independent asset supply on GitHub Pages. Full asset packs need not be committed.

KayKit Adventurers, Skeletons, Medieval Hexagon and Dungeon Remastered: Kay Lousberg, CC0. Original licenses are available at each source in the manifest. Babylon.js is Apache-2.0. No actual third-party binaries are included in this source-only archive.

## Test and verification status
- JavaScript syntax checked with Node; quest/combat, inventory and save-state tests are included in `tests/state.test.js`.
- Upstream repo trees and CC0 licenses verified. Six actual environment glTF/GLB payloads were inspected for mesh and texture metadata: cottage, tree, castle, wall, torch and treasure chest. Actual character GLB payloads and the live scene were not available in the isolated environment. The engine's runtime Diagnostics button reports loaded meshes, materials, textures, animation groups and FPS; review them on the target device.
- Offline Chromium browser-shell smoke tests passed at 390×844 and 844×390 with a deliberately blocked engine download: responsive layout, visible error and Retry. Browser 3D rendering / iPhone Safari gameplay and performance have not been verified. The code includes resolution controls, reused asset containers, a 1024 shadow map, fog, limited point lights, safe-area UI and pointer cancellation. These are design optimizations, not measured FPS guarantees.
- GitHub write access was rejected (403), so this is a local source delivery, not a deployed game.

## Next acceptance checks
Run `node --check 3d/game.js` and `node 3d/tests/state.test.js`.
Serve with any static HTTP server or GitHub Pages, then check loading, character/animation appearance, camera framing, collisions, complete quest, save/reload, touch controls, portrait/landscape and FPS. Do not expand the world until this gate passes.
