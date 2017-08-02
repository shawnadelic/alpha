#!/usr/bin/env python

import os
import shutil
import subprocess


AFFIRMATIVE_RESPONSES = ('y', 'yes')
FILES_WITH_REPLACEMENTS = ['manage.py', 'alpha/urls.py', 'alpha/settings/base.py', 'alpha/wsgi.py']

base_path = os.getcwd()
base_settings_path = os.path.join(base_path, 'alpha/settings/base.py')

# Ask whether or not to delete old git info
delete_git = raw_input('Delete .git directory? ').lower()
if delete_git in AFFIRMATIVE_RESPONSES:
    print 'Deleting .git directory'
    shutil.rmtree(os.path.join(base_path, '.git'))

# Ask for project name and replace in files
project_name = raw_input('Project name? (Example: SOME_SITE) ').lower()

settings_src_path = os.path.join(base_path, 'alpha')
settings_dest_path = os.path.join(base_path, project_name)

for path in FILES_WITH_REPLACEMENTS:
    file_path = os.path.join(base_path, path)
    subprocess.call(['sed', '-i', '-e', 's/ALPHA/{}/g'.format(project_name.upper()), file_path])
    subprocess.call(['sed', '-i', '-e', 's/alpha/{}/g'.format(project_name.lower()), file_path])

# Rename main project directory
os.rename(settings_src_path, settings_dest_path)

# Delete this setup script
os.remove(os.path.abspath(os.path.realpath(__file__)))

# If creating new repo, initialize new repo
if delete_git:
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
