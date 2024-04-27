from yaxp import xpath

from . import Control

from acre.lib import log


class Description(Control):
    def __init__(self, text=None, parent=None, **kwargs):
        super().__init__(parent)

    @property
    def text(self):
        return self.locator.get_text()

    @property
    def locator(self):
        return self.parent.locator(xpath.dd)


class DescriptionTerm(Control):
    def __init__(self, term=None, parent=None, **kwargs):
        super().__init__(parent=parent)
        self._kwargs = kwargs
        self._term = term

    @property
    def locator(self):
        kwa = self._kwargs.copy()
        if self._term:
            kwa['_'] = self._term
        xp = str(xpath.dt(**kwa))
        log.warning(str(xp))
        return self.parent.locator(xp)

    @property
    def description(self):
        return self.parent.locator(xpath.dd.following(self.locator))

    def with_description(self):
        return None
