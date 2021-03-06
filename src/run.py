#!/usr/bin/env python
#######################################################################
# This file is part of Lyntin.
# copyright (c) Free Software Foundation 2001, 2002
#
# Lyntin is distributed under the GNU General Public License license.  See the
# file LICENSE for distribution details.
# $Id: runlyntin.pyw,v 1.1 2003/10/03 02:17:48 willhelm Exp $
#######################################################################
import sys
import os
import output
import fixes
import i18n
from platform_utils import paths
i18n.setup()
fixes.setup()
output.setup()

bootoptions = {"ui": "wx",
               "datadir": "",
               "moduledir": [os.path.join(paths.app_path(), "modules")],
               "readfile": [],
               "snoopdefault": 1}

if len(sys.argv) >= 2:
  bootoptions["readfile"] = [sys.argv[1]]

if __name__ == '__main__':
  import application
  import lyntin.engine
  lyntin.engine.main(bootoptions)

# Local variables:
# mode:python
# py-indent-offset:2
# tab-width:2
# End:
 