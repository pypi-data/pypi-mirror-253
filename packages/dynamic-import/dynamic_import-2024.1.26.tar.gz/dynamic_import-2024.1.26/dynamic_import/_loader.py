from sys import _getframe, modules
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
from .prep import prep_files

__all__ = 'auto_loader',
ERROR_MSG = '`auto_loader()` must be called from within `__init__.py`'


def auto_loader(*, recursive=True):
    ''' Automatically find & load all modules

        Type
            recursive: bool
            return:    None

        Example
            # 'pkg/__init__.py'
            >>> from importer import auto_loader
            ...
            >>> auto_loader()

        Note
            - This function is useful when you want to load all the modules/sub-dir modules,
            like in case of website that needs to initialize `@link()` on runtime.
            - This is not dynamic, just loads modules.
    '''
    raise NotImplementedError('need to rewrite + test')
    caller = _getframe(1).f_globals  # get info of where `auto_loader()` is being called from
    try:
        package = caller['__package__']
        pkg_file = caller['__file__']
    except (KeyError, IndexError):
        raise ImportError(ERROR_MSG) from None

    if not package or not pkg_file.endswith('/__init__.py'):
        raise ImportError(ERROR_MSG)

    for module_name, module_path in prep_files(pkg_file, recursive=recursive):
        print('module_name:', module_name, 'module_path:', module_path)
        if module_name not in modules:
            loader = SourceFileLoader(module_name, module_path)
            spec = spec_from_loader(loader.name, loader)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
