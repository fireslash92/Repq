# Asset inspection — initial slice

## Verified directly from the upstream glTF/GLB metadata

| Asset | Meshes / texture evidence | Bounds / dependencies |
| --- | --- | --- |
| Blue cottage A | `building_home_A_blue`, `hexagons_medieval` texture | `building_home_A_blue.bin` (55,348 bytes), `hexagons_medieval.png` |
| Tree A | `tree_single_A`, `hexagons_medieval` texture | `tree_single_A.bin` (3,340 bytes), `hexagons_medieval.png` |
| Blue castle | `building_castle_blue`, `hexagons_medieval` | Local position bounds approx. x ±0.988, y 0–3.979, z ±1.128 |
| Dungeon wall | `Cube.16044`, `dungeon_texture` | Position bounds x −2 to 2, y 0 to 4, z −0.5 to 0.5 |
| Lit torch | `Cylinder.021`, `dungeon_texture` | Position bounds x/z ±0.275, y −0.395 to 0.731 |
| Gold chest | `Cube.14743`, `Cube.14744`, `dungeon_texture` | Two separate meshes; no animations listed in inspected JSON |

The four pack repositories and original CC0 licenses were read. The Adventurers pack advertises rigged characters with 75 animations; the Skeletons pack advertises 90+ animations. This is pack documentation, not independently verified animation-group counts for the selected GLB files. The large character binaries could not be retrieved from the available connector. The vendor script reads their actual JSON chunks and the game lists the loaded animation groups at runtime.

## Art decisions

Stylized low-poly KayKit family throughout; amber sunlight, blue-green mist, muted grass and stone, cream/gold/teal interface. Procedural geometry is limited to ground surfaces and billboard text, not stand-in characters or architecture. Heights are normalized from actual model bounds at runtime. Village/forest/castle/crypt are a continuous compact valley map, not separate large world regions. The castle is a landmark; the crypt is a roofless dungeon courtyard for readable third-person navigation.

## Optimization decisions (not benchmarked)

Asset containers reused for static placements; character rigs cloned independently. Render-resolution limits, quality switch, a small character shadow map, limited point lights, deterministic prop placement, collision boundaries, and frame-delta cap. Browser rendering and animation/camera acceptance must occur before world expansion.
