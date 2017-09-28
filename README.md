Alpha Starter Project
---------------------

A personalized Django starter project.

To setup:

1. Clone to a local repository.

2. Run setup script:

        python setup.py

3. Define the following environmental variables (usually in your .bashrc file):

       * [PROJECT_NAME]_SETTINGS_MODULE i.e., `project_name.settings.local`
       * [PROJECT_NAME]_SECRET_KEY, i.e. `gNR0PJG678CThj`

4. If using virtualenv, make sure virtualenv is installed and run:

        cd /your/project/path
        virtualenv venv
        source venv/bin/activate

5. Run

        pip install -r requirements.txt

   to install required packages.
