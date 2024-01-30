#!/usr/bin/env python

"""Get Python configuration variables.

Usage: python getconfig.py VARIABLE

Used to extract variables from Python's Makefile, intended to be
called from Asap's Makefile.
"""

import sys
import distutils.sysconfig

if len(sys.argv) != 2:
    print(f"\nERROR: Got {len(sys.argv)-1} arguments, expected 1.\n\n", file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(-1)

key = sys.argv[1]
if key == "SITEPACKAGES":
    print(distutils.sysconfig.get_python_lib(plat_specific=True))
else:
    cfgDict = distutils.sysconfig.get_config_vars()
    if key == 'BLDLIBRARY':
        val = cfgDict.get(key, None)
        if not val:
            val = '-lpython{}'.format(cfgDict['VERSION'])
        print(val)
    else:
        print(cfgDict[key])
        
