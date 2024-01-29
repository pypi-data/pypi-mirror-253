:image: https://raw.githubusercontent.com/Tobi-De/falco/main/assets/falco-logo.svg
:description: A demonstration of the essential workflow of the Falco CLI, from generating a new project to creating CRUD views for a model.

Usage / Overview
================

This page shows the optimal version of the initial falco workflow, from the generation of a new project to the creation of CRUD views for it.
This is supposed to represent the initial experience of a Falco CLI user, so if you can't reproduce  this exact workflow described below without
any problems, it means there's a problem and please create a `new issue <https://github.com/Tobi-De/falco/issues/new>`_ for it.

Let's create a new project called `myjourney`, and the main app for it `entries`. Is is a journaling app, the entries app represent
every entry in the journal.

1. Generate a new falco project and move into it

    .. code-block:: bash

        falco start-project myjourney && cd myjourney


2. Create a new virtual environment with for the project and install dependences

    .. code-block:: bash

        hatch shell


3. Initialite git and install pre-commit hooks

    .. code-block:: bash

        git init && pre-commit install

    Adjust the value python_version in the .pre-commit-config.yaml file if needed.

4. Create a new `.env` file

    .. code-block:: bash

        falco sync-dotenv

5. Fill in some values for the admin user

    .. code-block:: text
        :caption: .env

        DJANGO_SUPERUSER_EMAIL=admin@mail.com
        DJANGO_SUPERUSER_PASSWORD=admin

6. Migrate and setup and create the admin user

    .. code-block:: bash

        hatch run migrate && falco setup-admin

7. Create the new app ``entries``

    .. code-block:: bash

        falco start-app entries

8. Add some fiels to your ``Entry``

    .. code-block:: python

        class Entry(TimeStampedModel):
            # the TimeStampedModel adds the fields `created` and `modified` so we don't need to add them
            title = models.CharField(max_length=255)
            content = models.TextField()
            created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)


9.  Make migrations and migrate for the model

    .. code-block:: bash

        hatch run makemigrations && hatch run migrate

10. Generate crud views for the ``Entry`` model

    .. code-block:: bash

        falco crud entries.entry --entry-point --skip-git-check

11. Run your project

    .. code-block:: bash

        falco work

Now checkout `http://127.0.0.1:8000/entries` to see your running app.

That's like 10 commands, for the result it get us, not so bad, but could be much better, for any suggestion on how to improve (reduce the steps) this
worklow, feel free to open a discussions at https://github.com/Tobi-De/falco/discussions.

.. todo::

    Add screenshorts or give of the process and the resulting running app here.
