Alpha Starter Project
---------------------

A personalized Django starter project.

To setup:

1. Clone to a local repository.

2. Run

        rm -rf .git

   to delete git history.

3. Set `PROJECT_NAME_PREFIX` in `alpha.settings.base` to your project name.

4. Define the following environmental variables:

       * [PROJECT_NAME_PREFIX]_SETTINGS_MODULE i.e., `project_name.settings.local`
       * [PROJECT_NAME_PREFIX]_SECRET_KEY, i.e. `gNR0PJG678CThj`

5. Rename the `alpha` directory to your project name.

6. Update imports in `manage.py` and `settings.base` to match your change in step 5.

7. Run

        pip install -r requirements.txt

   to install required packages.
