.. linux_packages.rst

Linux packages management
=========================

List all installed packages with a short description:

.. code-block:: bash

   $ dpkg-query -l

List of packages installed:

.. code-block:: bash

   $ dpkg --get-selections | grep -v deinstall

Another option:

.. code-block:: bash

   $ apt list --installed

To copy the same packages in another server:

.. code-block:: bash

   $ dpkg --get-selections | grep -v deinstall > mypackages.txt
   $ scp mylist.txt user@server2:~/
   $ sudo apt-get install -y $(< mylist.txt)
   $ sudo apt-get autoremove
