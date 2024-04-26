from radish import before, after

from acre.lib import settings
from acre.playwright import Browser


@before.all(order=10)
def open_browser_testrun(features, marker):
    _open_browser('testrun')


@after.all(oder=10)
def close_browser_testrun(features, marker):
    _close_browser('testrun')


@before.each_feature(order=10)
def open_browser_feature(feature):
    _open_browser('feature')


@after.each_feature(oder=10)
def close_browser_feature(feature):
    _close_browser('feature')


@before.each_scenario(order=10)
def open_browser_scenario(scenario):
    _open_browser('scenario')


@after.each_feature(oder=10)
def close_browser_scenario(scenario):
    _close_browser('scenario')


def _open_browser(level):
    if settings.playwright.browser.auto != level:
        return
    Browser.open()


def _close_browser(level):
    if settings.playwright.browser.auto != level:
        return
    Browser.close()
