.. templates.rst

Working with templates
======================

Concept
-------

Templates are composed of **static parts** and **template tags** (dynamic content)


Configuration
-------------

Create the templates directory in **~/projects/eb_proj/eb/**.

Inside the **templates** directory we have to create a new directory for each application.

In base.py (settings.py) create the variable TEMPLATE_DIR with:

.. code-block:: python

   TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

**BASE_DIR** stores the path to **eb** directory and **TEMPLATE_DIR** the path to **templates**

In base.py (settings.py) also update the **TEMPLATES** variable:

.. code-block:: python

   TEMPLATES = [
      ...
      'DIRS': [TEMPLATE_DIR, ]
      ...
   ]


Adding a template
-----------------

Inside eb/templates/fooapp/ create the **template.html** file:

.. literalinclude:: data/template.html


Creating a new view
-------------------

A **template context** is a Python dictionary that maps template variable
names with Python variables.

Inside **eb/fooapp/views.py** create a new view (function):

.. code-block:: python

   from django.shortcuts import render

   def template(request):
      context_dict = {'message': "Hello from template"}
      return render(request,'fooapp/template.html',context=context_dict)


Check it works
--------------

.. code-block:: bash

   $ uwsgi --socket conf/eb.sock --module conf.wsgi --chmod-socket=666


Template inheritance
====================

Inside **/eb/templates/fooapp/** create the base.html file:

.. literalinclude:: data/base.html

Inside **/eb/templates/** create the base_0.html file:

.. literalinclude:: data/base_0.html

.. warning::
   Create a new view and the corresponding url.
