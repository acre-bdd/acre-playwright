import time

from radish import world

from acre.lib import retry
from acre.playwright import TimeoutError


class Control:
    def __init__(self, locator=None, parent=None):
        self._locator = locator
        self._parent = parent

    @property
    def locator(self):
        if self._locator:
            return self._locator
        return self.parent.locator(self.name)

    @property
    def parent(self):
        if self._parent:
            if isinstance(self._parent, Control):
                return self._parent.locator
            return self._parent
        return world.page

    def wait_for(self, *args, **kwargs):
        self.locator.wait_for(*args, **kwargs)

    def exists(self, *args, timeout=5000, **kwargs):
        try:
            self.locator.first.wait_for(*args, timeout=timeout, **kwargs)
            return True
        except TimeoutError:
            return False

    def click(self):
        self.locator.click()

    def clear(self, catch=False, timeout=1):
        if catch:
            self.wait_for(timeout=timeout * 1000)
        retry(fnc=lambda: not self.exists(timeout=timeout), message=f"clear(): {str(self)}")
        time.sleep(0.2)

    def __str__(self):
        if self._locator:
            return str(self._locator)
        return "Control"
