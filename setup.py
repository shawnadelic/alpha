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

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def replace_in_files(project_name):
    for path in FILES_WITH_REPLACEMENTS:
        file_path = os.path.join(BASE_PATH, path)
        subprocess.call(['sed', '-i', '-e', 's/ALPHA/{}/g'.format(project_name.upper()), file_path])
        subprocess.call(['sed', '-i', '-e', 's/alpha/{}/g'.format(project_name.lower()), file_path])


def initialize_repo():
    subprocess.call(['cd', base_path])
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
    project_dest_dir = os.path.join(BASE_PATH, project_name)
    replace_in_files(project_name)

    # Move main project directory
    project_src_dir = os.path.join(BASE_PATH, 'alpha')
    shutil.move(project_src_dir, project_dest_dir)

    # Delete the old README and write new file
    readme_path = os.path.join(BASE_PATH, 'README.md')
    os.remove(readme_path)
    with open(readme_path, 'wb') as readme_file:
        readme_str = '{}\n{}'.format(project_name.capitalize(), '=' * len(project_name))
        readme_file.write(readme_str)

    # Delete this setup script
    os.remove(os.path.abspath(os.path.realpath(__file__)))

    # If creating new repo, initialize new repo
    if delete_repo:
        initialize_repo()


if __name__ == '__main__':
    setup()
