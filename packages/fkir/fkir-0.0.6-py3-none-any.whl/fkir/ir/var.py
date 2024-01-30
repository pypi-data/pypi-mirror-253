from .base import FkBase


class FkVar(FkBase):
    def __init__(self, unqn=None) -> None:
        if unqn is None:
            unqn = self.get_default_unqn("var")

        super().__init__(unqn=unqn)

        self._srcs = set()
        self._dsts = set()

    @property
    def srcs(self):
        return self._srcs.copy()

    @property
    def dsts(self):
        return self._dsts.copy()

    def _add_src(self, node):
        self._srcs.add(node)

    def _remove_src(self, node):
        self._srcs.remove(node)

    def _add_dst(self, node):
        self._dsts.add(node)

    def _remove_dst(self, node):
        self._dsts.remove(node)
