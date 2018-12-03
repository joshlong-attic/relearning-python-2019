bonjour-pyramid
===============

In order to create this i had to download `cookiecutter`. `pip install cookiecutter`.
Cookiecutter in turn requires that you have `backports.functools_lru_cache`, but for Python 2. So:

```
pip2 uninstall backports.functools_lru_cache
pip2 install backports.functools_lru_cache
```


Getting Started
---------------

- Change directory into your newly created project.

    cd bonjour_pyramid

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.

        env/bin/alembic -c development.ini revision --autogenerate -m "init"

    - Upgrade to that revision.

        env/bin/alembic -c development.ini upgrade head

- Load default data into the database using a script.

    env/bin/initialize_bonjour_pyramid_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
