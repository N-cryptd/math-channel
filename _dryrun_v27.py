import py_compile
import importlib.util

py_compile.compile('scripts/undergraduate/video-27-matrices-as-transformations.py', doraise=True)
print('PY_COMPILE OK')

spec = importlib.util.spec_from_file_location('v27', 'scripts/undergraduate/video-27-matrices-as-transformations.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
cls = mod.Video27_MatricesAsTransformations
print('class found:', cls.__name__)
print('scene methods:', sorted(m for m in dir(cls) if m.startswith('scene')))

# Static wait audit: total wait time across scene methods (sanity, not authoritative)
import re
src = open('scripts/undergraduate/video-27-matrices-as-transformations.py').read()
pacing_comments = re.findall(r'# pacing: extends previous caption slot \(seg#(\d+) natural ([\d.]+)s, slot ([\d.]+)s -> ([\d.]+)s', src)
total_delta = sum(float(s) - float(o) for _, _, o, s in pacing_comments)
print(f'pacing comments: {len(pacing_comments)} (expect 19)')
print(f'total added slot time: {total_delta:.1f}s (expect ~121.5)')
req = lambda n: 1.08 * float(n) + 0.3
fails = [seg for seg, nat, old, new in pacing_comments if float(new) + 0.0001 < req(nat)]
print('segments below 1.08x+0.3:', fails if fails else 'NONE — all pass')
