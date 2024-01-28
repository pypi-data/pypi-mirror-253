:image: https://raw.githubusercontent.com/Tobi-De/falco/main/assets/falco-logo.svg
:description: A demonstration of the essential workflow of the Falco CLI, from generating a new project to creating CRUD views for a model.

Usage / Example
===============

This page shows the optimal version of the initial falco workflow, from the generation of a new project to the creation of CRUD views for it.
This is supposed to represent the initial experience of a Falco CLI user, so if you can't reproduce  this exact workflow described below without
any problems, it means there's a problem and please create a `new issue <https://github.com/Tobi-De/falco/issues/new>`_ for it. 

Let's create a new project called `myjourney`, and the main app for it `entries`. Is is a journaling app, the entries app represent 
every entry in the journal.

1. Generate a new falco project

    .. code-block:: bash

        falco start-project myjourney

2. Cd into the project directory

    .. code-block:: bash

        cd myjourney

3. Create a new virtual environment with for the project and install dependences

    .. code-block:: bash

        hatch shell


4. Initialite git and install pre-commit hooks

    .. code-block:: bash

        git init
        pre-commit install

5. Create a new `.env` file

    .. code-block:: bash

        falco sync-dotenv

6. Fill in some values for the admin user

    .. code-block:: text
        :caption: .env

        DJANGO_SUPERUSER_EMAIL=admin@mail.com
        DJANGO_SUPERUSER_PASSWORD=admin

7. Create the admin user

    .. code-block:: bash

        falco setup-admin

8. Create the new app `entries`

    .. code-block:: bash

        falco start-app entries

9. Add some fiels to your ``Entry`` model

    .. code-block:: python

        class Entry(TimeStampedModel):
            # the TimeStampedModel adds the fields `created` and `modified` so we don't need to add them
            title = models.CharField(max_length=255)
            content = models.TextField()
            created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)

10. Run your project

    .. code-block:: bash

        falco work


That's like 10 commands, for the result it get us, not so bad, but could be much better, for any suggestion on how to improve (reduce the steps) this 
worklow, feel free to open a discussions at https://github.com/Tobi-De/falco/discussions.

.. todo::

    Add screenshorts or give of the process and the resulting running app here.