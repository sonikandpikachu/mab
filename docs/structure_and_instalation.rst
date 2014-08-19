**********************************************************
Project structure, main design ideas and instalation guide
**********************************************************

General Structure:
----------

1. mab_angular - folder with angular part of the project.
2. mab_django - folder with django part of the project.
3. docs - project documentation
4. Makefile - file with main project commands


Django Instalation
------------------

1. Create postgres user and db:

    .. code:: sql

        CREATE USER mabuser WITH PASSWORD 'mabpassword';
        CREATE DATABASE mab ENCODING 'utf-8';
        GRANT ALL PRIVILEGES ON DATABASE mab to mabuser;

2. Install requirements:

    .. code:: bash

        pip install -r requirements/dev.txt

3. Init custom settings: cp mab_django/settings/custom.py.def mab_django/settings/custom.py

3. Init database: make syncdb

4. Run tests: make test

5. Start site: make run


Django details:
---------------

1. Settings: all settings are located in folder mab_django/settings:

   - base - main settings file, defines settings which are equal for all users and site states.
   - buildbot - settings for buildbot builds.
   - dev - settings for development.
   - production and staging(if exists) - settings for concrete server(without secret info).
   - test - settings for testing.
   - custom - non-in-git settings - secret keys and other secret info for each machine.

2. Core - base app without models but with general helpers, utils and abstract objects.



Angular instalation:
--------------------

1. Install Yeoman and angular generator for him. (Details: https://github.com/yeoman/generator-angular)

2. TODO...

