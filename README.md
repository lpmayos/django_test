django_test
===========

Small project to play a little bit with **Django** and **Django Rest Framework**.

It implements some demo models, and offers interaction with them through a **restful API** (http://localhost:8000/).

You'll find API documentation on http://localhost:8000/docs thanks to **rest_framework_swagger**


How to use it
-------------

::
  
    $ git clone git@github.com:lpmayos/django_test.git
    $ cd django_test/
    $ vagrant up --provision
    $ vagrant ssh
    vagrant@precise64:~$ cd /vagrant/
    vagrant@precise64:/vagrant$ source /home/vagrant/4dlife-env/bin/activate
    (4dlife-env)vagrant@precise64:/vagrant$ cd src/
    (4dlife-env)vagrant@precise64:/vagrant/src$ python manage.py runserver 0.0.0.0:8000
    
    Go to you browser and open http://localhost:8000 or http://localhost:8000/docs
