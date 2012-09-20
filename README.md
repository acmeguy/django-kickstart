django-kickstart
================

An attempt to create a private django kickstart, please view this as "learn by doing" exceercise rather than a viable option for anyone other than me.

Included packages

* django-crispy-forms - for better form handling and twitter-bootstrap compatibility
    * http://django-crispy-forms.readthedocs.org/en/d-0/install.html#installing-django-crispy-forms
    * https://github.com/maraujop/django-crispy-forms


Other requirements

Postgresql
==========

I like to use postgresql for development

Install at lease 9.2 (has some functionality I would like to explore)
```
sudo add-apt-repository ppa:pitti/postgresql
sudo apt-get update
sudo apt-get install postgresql-9.2
```
Configure postgresql for remote access (valid for ubunto and my network):
```
sudo su postgres

vim /etc/postgresql/9.2/main/postgresql.conf
* listen_addresses = '*'

vim /etc/postgresql/9.2/main/pg_hba.conf
host all all 192.168.1.0/24 trust

/etc/init.d/postgresql restart

```