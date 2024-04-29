# flake8: noqa: F401
import os

from .Control import Control
from .XPControl import XPControl
from .Link import Link
from .Input import Input

from acre.controls import factory

cfgfile = os.path.join(os.path.dirname(__file__), "controls.yml")

factory.register(cfgfile)
