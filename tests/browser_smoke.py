"""Optional cloud test: python -m playwright install chromium; python tests/browser_smoke.py.
Offline failure handling and responsive layout only; not a rendering acceptance test.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for w,h in [(390,844),(844,390)]:
        page=browser.new_page(viewport={'width':w,'height':h},is_mobile=True,has_touch=True,device_scale_factor=3)
        page.route('https://cdn.jsdelivr.net/**',lambda route:route.abort())
        # Inline local source to exercise the UI even when the browser blocks loopback.
        html=(root/'index.html').read_text().replace('<link rel="stylesheet" href="game.css">','<style>'+(root/'game.css').read_text()+'</style>')
        for name in ['state.js','game.js']:
            html=html.replace('<script src="'+name+'"></script>','<script>'+(root/name).read_text()+'</script>')
        page.set_content(html,wait_until='domcontentloaded')
        page.locator('#retry').wait_for(state='visible')
        assert 'Unable to load the world' in page.locator('#loadtext').inner_text()
        assert page.evaluate('document.documentElement.scrollWidth===innerWidth')
        assert page.locator('#retry').bounding_box()['width']>=44
        print(f'PASS: {w}x{h} responsive shell and visible retry on blocked engine')
        page.close()
    browser.close()
