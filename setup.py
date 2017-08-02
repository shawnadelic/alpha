#!/usr/bin/env python

import os
import shutil
import sys


AFFIRMATIVE_RESPONSES = ('y', 'yes')

delete_git = raw_input('Allow script to delete old git info? ').lower()

if delete_git in AFFIRMATIVE_RESPONSES:
    shutil.rmtree(os.path.join(os.getcwd(), '.git'))
else:
    print 'Must delete git info to proceed. Exiting setup...'
    sys.exit(1)

prefix = raw_input('Project prefix? (Example: SOME_SITE) ').upper()
