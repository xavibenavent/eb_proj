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

Modify the following settings to allow a **User Authenticated FTP Configuration**

1. anonymous_enable=NO
2. write_enable=YES
3. anon_upload_enable=NO
4. anon_mkdir_write_enable=NO

Restart the vsftpd server and check it:

.. code-block:: bash

   $ sudo service vsftpd restart
   $ sudo service --status-all



Basic Atom setup
----------------

When starting:

1. Download Atom (.deb or .rpm)
2. Install package **remote-ftp** from within Atom
3. Open and set **.ftpconfig** file to allow a **User Authenticated FTP Configuration**
   to connect to **/xbn/home/projects/**

.. literalinclude:: data/ftpconfig.data


4. From packages>remote-ftp **Toggle**
5. From packages>remote-ftp **Connect**



When finishing:

1. From packages>remote-ftp> **Disconnect**
