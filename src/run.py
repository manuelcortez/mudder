#!/usr/bin/env python
#######################################################################
# This file is part of Lyntin.
# copyright (c) Free Software Foundation 2001, 2002
#
# Lyntin is distributed under the GNU General Public License license.  See the
# file LICENSE for distribution details.
# $Id: runlyntin.pyw,v 1.1 2003/10/03 02:17:48 willhelm Exp $
#######################################################################
bootoptions = {"ui": "wx",
               "datadir": "",
               "moduledir": [],
               "readfile": [],
               "snoopdefault": 1}

import sys
import fixes
fixes.setup()
import output
output.setup()
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
 