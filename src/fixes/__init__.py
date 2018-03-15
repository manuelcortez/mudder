# -*- coding: utf-8 -*-
import sys
if hasattr(sys, "frozen"):
	import fix_win32com

def setup():
	if hasattr(sys, "frozen"):
		fix_win32com.fix()
