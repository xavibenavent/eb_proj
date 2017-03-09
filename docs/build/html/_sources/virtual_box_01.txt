.. virtual_box_01.rst

Tips when accessing VirtualBox GUEST machine from HOST machine
==============================================================


In the following configuration:

.. note::

   <browser in HOST machine> <------> <Django server in GUEST (VirtualBox)>

To allow access from the HOST machine through NATS, we have to start
the Django development server with 0.0.0.0:

.. code-block:: bash

   $ python manage.py runserver --settings=conf.settings.production 0.0.0.0:8000

Or:

.. code-block:: bash

   $ ... 192.168.56.101:8000 instead of 0.0.0.0:8000

.. warning::
   In the file confs/settings/production.py it is not necessary to use the **asterisk** inside ALLOWED_HOSTS

.. warning::
   In PRODUCTION it will be necessary.


Check Django server typing at the browser:

.. code-block:: HTML

  http://192.168.56.101:8000


If we are accessing the Django server from the same machine, then:

.. code-block:: bash

   $ python manage.py runserver --settings=conf.settings.production

From the GUEST machine we can access the Django server:

.. code-block:: bash

   $ curl 127.0.0.0:8000
