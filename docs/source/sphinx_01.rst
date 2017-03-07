Using Sphinx
============

First steps
-----------

Download & Install Sphinx:

.. code-block:: console

   $ sudo pip install Sphinx

.. warning:: When pulling from a repository it is better to install sphinx as a linux package.
             (We will recognize this situation when the **$ make html** command won't work).
             Installation: **$ sudo apt-get install python-sphinx**

Create the directory to hold the project

.. code-block:: console

   $ mkdir sf01
   $ cd sf01

Create the working structure and follow the guided questions:

.. code-block:: console

   $ sphinx-quickstart [options] [projectdir]
   #$ sphinx-quickstar sf01
   #$ sphinx-quickstar --quiet --project=sf01 --author=xbn -v 1.0

Check the created files:

.. code-block:: console

   $ ls -AR


Check **index.rst** file:

.. include:: index.rst
   :literal:

Check **conf.py** file:

.. include:: conf.py
   :literal:

Start the python built-in web server:

.. code-block:: console

   $ python -m simpleHTTPServer 8000

Test with a web browser:

.. code-block:: none

    http://192.168.56.101:8000


Creating documentation
----------------------

Edit the **index.rst** file and add the **ch_XX.rst** files needed


Main directives
---------------

**Paragraph:**

This is a paragraph

**Code:**

.. code-block:: bash

   $ command parameter

**List:**

1. First item
2. Second item

**File content:**

.. include:: foofile.data
   :literal:
