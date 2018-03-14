# -*- coding: utf-8 -*-
""" This module contains some bugfixes for packages used in TWBlue."""
import sys
from . import fix_win32com
def setup():
	if hasattr(sys, "frozen"):
		fix_win32com.fix()