import importlib.util

spec = importlib.util.spec_from_file_location('v112', 'scripts/undergraduate/video-112-subgroups-and-cyclic-groups.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
cls = mod.Video112_SubgroupsAndCyclicGroups
print('class found:', cls.__name__)
print('scene methods:', sorted(m for m in dir(cls) if m.startswith('scene')))
