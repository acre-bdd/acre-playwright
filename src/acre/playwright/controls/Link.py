from yaxp import xpath

from . import Control

from acre.lib import log


class Link(Control):
    def __init__(self, text=None, target=None, parent=None, **kwargs):
        super().__init__(parent=parent)
        self._kwargs = kwargs
        self._text = text
        self._target = target

    @property
    def locator(self):
        kwa = self._kwargs.copy()
        if self._text:
            kwa['_'] = self._text
        xp = str(xpath.a(**kwa))
        log.warning(str(xp))
        return self.parent.locator(xp)
