from __future__ import annotations

import importlib.util
import sys


def __getattr__(name: str) -> object:
    """Defer importing own modules until attempting to access an attribute.

    Importing this in ``__init__`` will overwrite relative imports.
    """
    fullname = __spec__.parent + '.' + name
    try:
        return sys.modules[fullname]
    except KeyError:
        spec = importlib.util.find_spec(fullname)
        if spec is None:
            # ``AttributeError`` is converted to an ``ImportError`` by the import machinery
            raise AttributeError from None

        sys.modules[fullname] = module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            raise AttributeError from None

        lazy_loader = importlib.util.LazyLoader(spec.loader)
        lazy_loader.exec_module(module)
        return module
