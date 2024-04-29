from yaxp import xpath as xp
from radish import world

from acre.lib import log

from acre.playwright.controls import Control


class XPControl(Control):
    def __init__(self, parent=None, config=None, **kwargs):
        super().__init__(parent=parent)
        self._config = config
        self._parent = parent
        self._kwargs = kwargs

    @property
    def locator(self):
        if self.parent:
            return self.parent.locator(str(self.xpath))
        return world.page.locator(str(self.xpath))

    @property
    def xpath(self):
        args = self._config
        if self._kwargs:
            args.update(self._kwargs)
        log.warning(f"xpath: {args}")
        _xp = xp.by(**args)
        log.warning(str(_xp))
        return _xp
