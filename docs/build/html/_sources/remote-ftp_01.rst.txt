# remote-ftp_01.rst

Using Atom remote-ftp package
=============================

Basic linux (Ubuntu) setup
--------------------------

Install **vsftpd**:

.. code-block:: bash

   $ sudo apt-get istall vsftpd

Edit **/etc/vsftpd.conf** file:

.. code-block:: bash

   $ sudo vim /etc/vsftpd.conf

Modify the following settings:

1. anonymous_enable=YES
2. write_enable=YES
3. anon_upload_enable=YES
4. anon_mkdir_write_enable=YES

Restart the vsftpd server and check it:

.. code-block:: bash

   $ sudo service vsftpd restart
   $ sudo service --status-all



Basic Atom setup
----------------

When starting:

1. Install package **remote-ftp** from within Atom
2. Open and set **.ftpconfig** file
3. From packages>remote-ftp>Toggle
4. From packages>remote-ftp>Connect


When finishing:

1. From packages>remote-ftp>Disconnect
