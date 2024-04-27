# flake8: noqa: F401
from playwright.sync_api import expect, TimeoutError  # noqa: F401

from acre.lib import settings

from .browser import Browser

from .steps import basic, browser
from .hooks import playwright

from .hooks import autobrowser
from . import controls

from . import setup

setup.init()

import acre as _acre
_acre.controls = controls
