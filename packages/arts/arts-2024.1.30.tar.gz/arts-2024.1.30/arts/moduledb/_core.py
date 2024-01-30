from pathlib import Path
from tempfile import mkdtemp
from json import loads, dumps
from types import ModuleType
from os.path import abspath


root_dir = Path('~/.PyModuleDB').expanduser()
info_file = root_dir / 'info.json'
module_dirs = root_dir / 'module_dirs'

module_dirs.mkdir(parents=True, exist_ok=True)

if info_file.exists():
    info = loads(info_file.read_text('utf8'))
else:
    info = {'modules':{}}
modules = info['modules']


class File:

    path: Path
    level: int
    core: dict

    def __init__(self, path: str|Path, level: int):
        # path
        assert Path(path).suffix != '.mfile'
        self.path = path = Path(f"{path}.mfile")
        self.level = level
        # core
        if path.exists():
            # self.core 不要设置 caches 缓存, 否则缓存的 core 不会被自动回收, 会占据大量内存.
            self.core = loads(path.read_text('utf8'))
        else:
            self.core = {}

    def __setitem__(self, field, value):
        self.core[field] = value
        self.save()

    def __getitem__(self, field):
        return self.core[field]

    def get(self, field, default=None):
        return self.core.get(field, default)
    
    def setdefault(self, field, default=None):
        '''
        由于该函数是同步函数, 因此采用 if-else 结构是异步安全的.
        '''
        if field in self.core:
            return self.core[field]
        else:
            r = self.core.setdefault(field, default)
            self.save()
            return r
    
    def __ior__(self, obj):
        '''
        self |= obj
        '''
        if isinstance(obj, File):
            self.core |= obj.core
        else:
            self.core |= obj
        self.save()
        return self
    
    def __bool__(self): return bool(self.core)
    def __iter__(self): return self.core.__iter__()
    def keys(self): return self.core.keys()
    def values(self): return self.core.values()
    def items(self): return self.core.items()
    
    def update(self, obj):
        if isinstance(obj, File):
            r = self.core.update(obj.core)
        else:
            r = self.core.update(obj)
        self.save()
        return r
    
    def save(self):
        self.path.write_text(dumps(self.core, ensure_ascii=False), 'utf8')


class Dir:
    
    path: Path
    level: int
    depth: int

    def __init__(self, path: str|Path, level: int, depth:int):
        # path
        assert Path(path).suffix != '.mdir'
        self.path = Path(f"{path}.mdir")
        self.path.mkdir(parents=True, exist_ok=True)
        self.level = level
        self.depth = depth

    def abspath(self):
        return abspath(self.path)

    def __getitem__(self, name: str):
        path = self.path / name
        level = self.level + 1
        if level == self.depth:
            return File(path=path, level=level)
        else:
            return Dir(path=path, level=level, depth=self.depth)


class ModuleDB:

    path: Path
    depth: int

    def __init__(self, module: ModuleType|str, depth: int=2):
        if isinstance(module, ModuleType):
            mpath = abspath(module.__file__)
        else:
            assert type(module) is str
            mpath = module
        path = modules.get(mpath)
        if not path:
            path = modules[mpath] = abspath(mkdtemp(dir=module_dirs))
            info_file.write_text(dumps(info, ensure_ascii=False), 'utf8')
        self.path = Path(path)
        self.path.mkdir(exist_ok=True)
        self.depth = depth

    def abspath(self):
        return abspath(self.path)
    
    def __getitem__(self, name: str) -> Dir|File:
        path = self.path / name
        if self.depth == 1:
            return File(path=path, level=1)
        else:
            return Dir(path=path, level=1, depth=self.depth)