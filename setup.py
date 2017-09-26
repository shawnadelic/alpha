#!/usr/bin/env python

import os
import shutil
import subprocess


FILES_WITH_REPLACEMENTS = [
    'manage.py',
    'alpha/urls.py',
    'alpha/settings/base.py',
    'alpha/wsgi.py',
]

BASE_PATH = os.getcwd()


def replace_in_files(project_name):
    for path in FILES_WITH_REPLACEMENTS:
        file_path = os.path.join(BASE_PATH, path)
        subprocess.call(['sed', '-i', '-e', 's/ALPHA/{}/g'.format(project_name.upper()), file_path])
        subprocess.call(['sed', '-i', '-e', 's/alpha/{}/g'.format(project_name.lower()), file_path])


def initialize_repo():
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])


def get_boolean_response(text):
    response = raw_input('{} '.format(text)).lower()
    return response in ('y', 'yes')


def setup():
    # Ask whether or not to delete old repo info
    delete_repo = get_boolean_response('Delete existing repo?')
    if delete_repo:
        print 'Deleting existing repo'
        shutil.rmtree(os.path.join(BASE_PATH, '.git'))

    # Ask for project name and replace in files
    project_name = raw_input('Project name? (Example: SOME_SITE) ').lower()
    replace_in_files(project_name)

    # Rename main project directory
    shutil.move('alpha', project_name)

    # Delete the old README and write new file
    readme_path = os.path.join(BASE_PATH, 'README.md')
    os.remove(readme_path)

    with open(readme_path, 'wb') as readme_file:
        readme_file.write('{}\n{}'.format(project_name.capitalize(), '=' * len(project_name)))

    # Delete this setup script
    os.remove(os.path.abspath(os.path.realpath(__file__)))

    # If creating new repo, initialize new repo
    if delete_repo:
        initialize_repo()


if __name__ == '__main__':
    setup()
