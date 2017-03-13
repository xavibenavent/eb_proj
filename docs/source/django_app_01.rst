.. django_app_01.request

Working with a Django app
=========================

Creating a Django app
---------------------

From **(dj1.9) ~/projects/eb_proj/eb/** create the **fooapp** app:

.. code-block:: bash

   $ python manage.py startapp fooapp

Check the created files:

.. literalinclude:: data/tree_fooapp.data

Add **fooapp** to INSTALLED_APPS in **settings.py**.

Check the stack:

.. code-block:: bash

   $ uwsgi --socket conf/eb.sock --module conf.wsgi --chmod-socket=666



Creating a view
---------------

**fooapp/views.py**:

.. literalinclude:: data/fooapp.views.py

**conf/urls.py**:

.. literalinclude:: data/conf.urls.py

**foapp/urls.py**:

.. literalinclude:: data/fooapp.urls.py

Check the stack:

.. code-block:: bash

   $ uwsgi --socket conf/eb.sock --module conf.wsgi --chmod-socket=666

.. code-block:: bash

   http://127.0.0.1:8008/fooapp/
