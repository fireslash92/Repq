# Verification record

- PASS — `node --check game.js` and `node --check state.js`.
- PASS — `node tests/state.test.js`: quest gates, two turn-based encounters, skill/guard, potion, relic acquisition, chapter completion, duplicate reward prevention, saved-state normalization and defeat handling.
- PASS — `python tests/browser_smoke.py`: Chromium inlined static HTML/CSS/JS at 390×844 and 844×390, deliberate blocked engine download, responsive shell width and Retry button.
- PASS — `python -m py_compile vendor_selected.py`.
- NOT RUN — full repository clone and KayKit import. The environment cannot resolve GitHub via git, and the connector does not return large binary character models.
- NOT RUN — live Babylon 3D rendering, asset download and actual animation inspection, full browser quest run, actual iPhone Safari, GPU/FPS benchmarking. Browser loopback navigation is also blocked by administrator policy in this environment; the smoke test uses inlined static sources instead.
- NOT DEPLOYED — GitHub write requests returned 403 Resource not accessible by integration. The archive is a source-only overlay; the original repository was not changed.
