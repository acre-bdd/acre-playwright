# flake8: noqa: F401
from playwright.sync_api import expect, TimeoutError  # noqa: F401

from acre.lib import settings

from .browser import Browser
from .smartlocator import SmartLocator

from .steps import basic, browser
from .hooks import playwright

if settings.playwright.browser.auto:
    from .hooks import autobrowser

