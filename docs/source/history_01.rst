.. history_01.rst

History
=======

$ sudo apt-get update
$ sudo apt-get upgrade
# Install atom (.deb)
# Check git OK
# Check python3 (3.5.2+)
$ sudo apt-get install python-sphinx
$ sudo apt-get install virtualenv
$ mkdir .envs
$ cd .envs
$ virtualenv dj1.9 --python=python3.5
$ source dj1.9/bin/activate
(dj1.9) $ pip freeze
(dj1.9) $ pip install django==1.9
$ mkdir projects
