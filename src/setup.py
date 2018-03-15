# -*- coding: utf-8 -*-
""" Setup file to create executables and distribute the source code of this application. Don't forget this file! """
############################################################
#    Copyright (c) 2016 Manuel Cortez <manuel@manuelcortez.net>
#       
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################
from setuptools import setup, find_packages
import py2exe
import os
import platform
from glob import glob

def get_data():
 import accessible_output2
 import sound_lib
 return [
  ("accessible_output2/lib", glob("accessible_output2/lib/*.dll")),
 ]+get_sounds()+get_modules()+accessible_output2.find_datafiles()+sound_lib.find_datafiles()

def get_sounds():
 answer = []
 depth = 6
 for root, dirs, files in os.walk('sounds'):
  if depth == 0:
   break
  new = (root, glob(os.path.join(root, "*.ogg")))
  answer.append(new)
  depth -= 1
 return answer

def get_modules():
 answer = []
 depth = 6
 for root, dirs, files in os.walk("modules"):
  if depth == 0:
   break
  new = (root, glob(os.path.join(root, "*.py")))
  answer.append(new)
  depth -= 1
 return answer

if __name__ == '__main__':
 setup(
  name = "mudder",
  author = "Manuel Cortez",
  author_email = "manuel@manuelcortez.net",
  version = "0.1",
  url = "https://manuelcortez.net/mudder",
packages= find_packages(),
data_files = get_data(),
options = {
   'py2exe': {   
    'optimize':2,
   'packages': ["lyntin", "sound_lib", "code"],
    'dll_excludes': ["MPR.dll", "api-ms-win-core-apiquery-l1-1-0.dll", "api-ms-win-core-console-l1-1-0.dll", "api-ms-win-core-delayload-l1-1-1.dll", "api-ms-win-core-errorhandling-l1-1-1.dll", "api-ms-win-core-file-l1-2-0.dll", "api-ms-win-core-handle-l1-1-0.dll", "api-ms-win-core-heap-obsolete-l1-1-0.dll", "api-ms-win-core-libraryloader-l1-1-1.dll", "api-ms-win-core-localization-l1-2-0.dll", "api-ms-win-core-processenvironment-l1-2-0.dll", "api-ms-win-core-processthreads-l1-1-1.dll", "api-ms-win-core-profile-l1-1-0.dll", "api-ms-win-core-registry-l1-1-0.dll", "api-ms-win-core-synch-l1-2-0.dll", "api-ms-win-core-sysinfo-l1-2-0.dll", "api-ms-win-security-base-l1-2-0.dll", "api-ms-win-core-heap-l1-2-0.dll", "api-ms-win-core-interlocked-l1-2-0.dll", "api-ms-win-core-localization-obsolete-l1-1-0.dll", "api-ms-win-core-string-l1-1-0.dll", "api-ms-win-core-string-obsolete-l1-1-0.dll", "WLDAP32.dll", "MSVCP90.dll"],
   },
  },
  windows = [
   {
    'script': 'run.py',
    'dest_base': 'mudder',
}
  ],
  install_requires = [
  ]
 )
