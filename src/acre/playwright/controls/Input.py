from yaxp import xpath

from . import Control

from acre.lib import log


class Input(Control):
    def __init__(self, parent=None, config=None, **kwargs):
        super().__init__(parent=parent)
        self._config = config
        self._kwargs = kwargs

    @property
    def locator(self):
        kwa = self._kwargs.copy()
        xp = str(xpath.input(**kwa))
        log.warning(str(xp))
        return self.parent.locator(xp)
