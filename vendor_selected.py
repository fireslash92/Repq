"""Vendor pinned models, dependencies, licenses and Babylon UMD scripts in a network-enabled shell.
Run the repository's import_assets.py first if you want the full libraries.
"""
import argparse, json, pathlib, urllib.request, urllib.error, struct, urllib.parse
ROOT=pathlib.Path(__file__).resolve().parent
manifest=json.loads((ROOT/'asset-manifest.json').read_text())
out=ROOT/'assets'/'selected'
out.mkdir(parents=True,exist_ok=True)
version='7.54.3'
def fetch(url,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    if not path.exists():
        with urllib.request.urlopen(url,timeout=90) as response: data=response.read()
        if data.startswith(b'version https://git-lfs.github.com/spec/v1'): raise ValueError('LFS pointer: '+url)
        path.write_bytes(data)
    return path.read_bytes()
def parse(data):
    if data[:4]==b'glTF':
        n,kind=struct.unpack_from('<II',data,12)
        if kind!=0x4e4f534a: raise ValueError('Bad GLB JSON')
        return json.loads(data[20:20+n])
    return json.loads(data)
def main():
    report={}
    for name,a in manifest.items():
        target=ROOT/a['local']; data=fetch(a['url'],target); j=parse(data)
        for item in j.get('buffers',[])+j.get('images',[]):
            uri=item.get('uri','')
            if uri and not uri.startswith('data:'):
                if '://' in uri or '..' in pathlib.PurePosixPath(uri).parts: raise ValueError('Unsafe URI: '+uri)
                fetch(urllib.parse.urljoin(a['url'],uri),target.parent/uri)
        license_url='https://raw.githubusercontent.com/'+a['repository']+'/'+a['revision']+'/LICENSE.txt'
        fetch(license_url,out/a['pack']/'LICENSE.txt')
        report[name]={'meshes':len(j.get('meshes',[])),'materials':len(j.get('materials',[])),'textures':len(j.get('textures',[])),'animations':[x.get('name') for x in j.get('animations',[])],'skins':len(j.get('skins',[])),'bytes':len(data)}
        print(name, report[name]['bytes'], 'bytes', len(report[name]['animations']), 'animations')
    (out/'inspection.json').write_text(json.dumps(report,indent=2))
    (out/'READY.json').write_text(json.dumps({'ready':True}))
    vendor=ROOT/'vendor'
    for package,file in [('babylonjs','babylon.js'),('babylonjs-loaders','babylonjs.loaders.min.js')]:
        fetch('https://cdn.jsdelivr.net/npm/'+package+'@'+version+'/'+file,vendor/file)
        for filename in ['license.md','LICENSE','LICENSE.md','license.txt']:
            try:
                fetch('https://cdn.jsdelivr.net/npm/'+package+'@'+version+'/'+filename,vendor/(package+'-LICENSE.md'))
                break
            except urllib.error.HTTPError:
                continue
        else:
            raise RuntimeError('Could not find package license: '+package)
    (vendor/'READY.json').write_text(json.dumps({'version':version}))
    print('Vendored selected models and engine. Review assets/selected/inspection.json.')
if __name__=='__main__': main()
