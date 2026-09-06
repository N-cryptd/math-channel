import importlib.util

spec = importlib.util.spec_from_file_location('v28', 'scripts/undergraduate/video-28-matrix-multiplication.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
cls = mod.Video28_MatrixMultiplication
print('class found:', cls.__name__)
print('scene methods:', sorted(m for m in dir(cls) if m.startswith('scene')))
