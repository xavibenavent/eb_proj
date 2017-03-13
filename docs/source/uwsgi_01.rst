# uwsgi_01.rst

uWSGI server
============

uWSGI installation
------------------

Install the **python3.5-dev** package:

.. code-block:: bash

   $ sudo apt-get install python3.5-dev

Check that **uwsgi** is not installed as a global
package (deactivate any virtual environment first):

.. code-block:: bash

   $ pip freeze

uWSGI installation in the virtual environment (activate the virtual
environment first):

.. code-block:: bash

   $ sudo pip install uwsgi


Check **web client <-> uWSGI <-> Python**
-----------------------------------------

Create the file **test.py** into the **conf** directory:

.. literalinclude:: data/test.py

Run uWSGIfrom the **~/projects/eb_proj/eb/** directory:

.. code-block:: bash

   $ uwsgi --http :8000 --wsgi-file conf/test.py

Check with the browser to **127.0.0.1:8000**


Check **web client <-> Django project**
---------------------------------------

From the **~/projects/eb_proj/eb/** directory, run the django
development server:

.. code-block:: bash

   $ python manage.py runserver 8001

Check with the browser to **127.0.0.1:8001**
We can also check admin at **127.0.0.1:8000/admin**


Check **web client <-> uWSGI <-> Django**
-----------------------------------------

Run uWSGIfrom the **~/projects/eb_proj/eb/** directory to
run the Django project:

.. code-block:: bash

   $ uwsgi --http :8000 --module conf.wsgi

Check with the browser to **127.0.0.1:8000**


Check **web client <-> web server (NGINX) <-> uWSGI <-> Django**
----------------------------------------------------------------

Check that NGINX server is running.

Run the Django application connecting NGINX and uWSGI through
a socket:

.. code-block:: bash

   $ uwsgi --socket conf/eb.sock --module conf.wsgi --chmod-socket=666
