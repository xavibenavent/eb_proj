.. nginx_01.rst

Using NGINX server
==================

Installation
------------

.. code-block:: bash

   $ sudo apt-get install nginx

Check installed files:

Binary file::

   /usr/sbin/nginx

Log files::

   /var/log/nginx/access.log
   /var/log/nginx/error.log

Configuration file::

   /etc/nginx/nginx.conf

.. note:: In this file there are settings as **worker_connections**


Configuration
-------------

The server also reads the settings contained in the files stored at
**/etc/nginx/sites-enabled/** directory.

We need to create a configuration file with:

1. Listening port
2. Socket to forward to uWSGI server
3. Absolut (hard-coded) path for static files
4. Absolut (hard-coded) path for media files

Contents of the configuration file **nginx.data**:
::

   /home/xbn/projects/eb_proj/servers_conf/nginx.data

Contents of the **nginx.data** file:

.. literalinclude:: data/nginx_01.data


But instead of storing the file in this directory,
we create a soft link to the file in our production directory:
::

   /etc/nginx/sites-enabled/nginx.data

We create the soft link:

.. code-block:: bash

   $ sudo ln -s /home/xbn/eb20/nexus/nexus_nginx.conf /etc/nginx/sites-enabled



Starting the server
===================

.. code-block:: bash

   $ sudo service nginx start (or restart)

Check that the server is running and listening to the apropriate port:

.. code-block:: bash

   $ ps -A | grep nginx
   $ sudo lsof -i
