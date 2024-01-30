import json
import os
from types import NoneType
from typing import Callable, Optional

from .base import ExtensionBase
from .dictx import DictX
from .listx import ListX

Dumpable = list | dict | ListX | DictX
Indent = Optional[int]


class JsonX:
    def __new__(cls, data, saver: Optional[Callable[[Dumpable], NoneType]] = None):
        klass = ExtensionBase.get_class(data, saver, init=True)
        if klass is not None:
            return klass
        else:
            raise ValueError(
                f"No appropriate class found for {data.__class__.__name__}")

    @classmethod
    def accept(cls, data, *init_args, **init_kwargs):
        for cls, superclass in ExtensionBase.classes.items():
            if isinstance(data, cls):
                return data
            elif (clsm := getattr(cls, "accept", None)) is not None:
                try:
                    parsed = clsm(data)
                    if not isinstance(parsed, cls | superclass): continue
                    return cls(parsed, *init_args, **init_kwargs)
                except Exception:
                    continue
        return data
    

def save(file: str, obj: Dumpable, indent: Indent = None):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=indent)


def load(file: str, indent: Indent = None):
    with open(file, encoding="utf-8") as f:
        return JsonX(json.load(f), saver=lambda d: save(file, d, indent))


def load_advanced(file: str, indent: Indent = None, content: Optional[Dumpable | str] = None, createCallback: Optional[Callable] = None):
    _created = False
    if content is not None and not os.path.exists(file):
        _dir = os.path.dirname(file)
        _dir and os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, "w", encoding="utf-8") as f:
            content = json.dumps(content) if isinstance(
                content, dict) else content
            f.write(content)
            _created = True

    if _created and createCallback is not None:
        createCallback()

    return load(file, indent)
