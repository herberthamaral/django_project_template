Django project template
=======================

Since django 1.4 it is possible to use project templates. This project template add some conventions to django in order
to ease django's initial learning curve. I've did this thinking of my students who struggle to initialize all the
required settings in a django project.

Here are some of the conventions:

- templates, media and static folders are already created a configured.
- auto url for media folder.
- index.html template, which allows editing of "It works" initial page.
- .gitgnore and requirements.txt files

How to use it
-------------

    $ django-admin.py startproject myproject --template=https://github.com/herberthamaral/django_project_template/archive/master.zip
    $ cd myproject
    $ python manage.py runserver

