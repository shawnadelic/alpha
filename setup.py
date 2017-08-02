#!/usr/bin/env python

import os
import shutil
import subprocess
import sys


AFFIRMATIVE_RESPONSES = ('y', 'yes')

base_path = os.getcwd()
base_settings_path = os.path.join(base_path, 'alpha/settings/base.py')

delete_git = raw_input('Allow script to delete old git info? ').lower()

if delete_git in AFFIRMATIVE_RESPONSES:
    #shutil.rmtree(os.path.join(dir_path, '.git'))
    pass
else:
    print 'Must delete git info to proceed. Exiting setup...'
    sys.exit(1)

project_name = raw_input('Project name? (Example: SOME_SITE) ').lower()

settings_src_path = os.path.join(base_path, 'alpha')
settings_dest_path = os.path.join(base_path, project_name)

subprocess.call(['sed', '-i', '-e', 's/ALPHA/{}/g'.format(project_name.upper()), base_settings_path])

os.rename(settings_src_path, settings_dest_path)
