django_test
===========

Small project to play a little bit with **Django**, and how it works with **neo4j** using **neomodel**.


How to use it
-------------

$ git clone git@github.com:lpmayos/django_test.git
$ cd django_test/
$ vagrant up --provision
$ vagrant ssh
vagrant@precise64:~$ cd /vagrant/
vagrant@precise64:/vagrant$ source /home/vagrant/4dlife-env/bin/activate
(4dlife-env)vagrant@precise64:/vagrant$ cd src/
(4dlife-env)vagrant@precise64:/vagrant/src$ python manage.py runserver 0.0.0.0:8000

Go to you browser and open localhost:8000
