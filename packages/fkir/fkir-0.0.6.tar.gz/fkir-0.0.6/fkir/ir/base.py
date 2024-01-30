import json
from typing import Any


class FkBase:
    unique_counter = {}

    def __init__(self, unqn=None) -> None:
        self._attr = {}
        if unqn is None:
            unqn = self.get_default_unqn("base")
        self._unqn = unqn

    @property
    def unqn(self):
        return self._unqn

    def vis_label(self):
        return self.unqn

    def get_default_unqn(self, prefix=""):
        cls = self.__class__
        if prefix not in cls.unique_counter:
            cls.unique_counter[prefix] = 0
        n = f"{prefix}_{cls.unique_counter[prefix]}"
        cls.unique_counter[prefix] += 1
        return n

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name.startswith("_") or isinstance(
            getattr(self.__class__, __name, None), property
        ):
            super().__setattr__(__name, __value)
        else:
            self._attr[__name] = __value

    def __getattr__(self, __name: str) -> Any:
        if __name.startswith("_") or isinstance(
            getattr(self.__class__, __name, None), property
        ):
            return object.__getattribute__(self, __name)
        else:
            try:
                return self._attr[__name]
            except KeyError:
                raise AttributeError(f"attr {__name} not found")

    def __repr__(self) -> str:
        return f"<{__class__}:{self.unqn}>"

    def __str__(self) -> str:
        return self.__repr__()

    def __hash__(self) -> int:
        return hash(self.unqn)
