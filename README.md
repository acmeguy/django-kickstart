django-kickstart
================

An attempt to create a private django kickstart, please view this as "learn by doing" exceercise rather than a viable option for anyone other than me.

Included packages

* docutils - just to get the django documentation working
* django-crispy-forms - for better form handling and twitter-bootstrap compatibility
    * https://github.com/maraujop/django-crispy-forms
    * http://django-crispy-forms.readthedocs.org/en/d-0/install.html#installing-django-crispy-forms
* django-tastypie - for all the REST API goodies
    * https://github.com/toastdriven/django-tastypie
* django-grapelli - Seem to be back on track with their admin replacement
    * https://github.com/sehmaschine/django-grappelli
    * http://django-grappelli.readthedocs.org/en/2.4.2/index.html
* django-filebrowser - for admin filebrowsing in grappelli
    *
    * http://django-filebrowser.readthedocs.org/en/latest/

Other requirements

Sqlite3
==========

```
# sudo apt-get install sqlite3  #If you want to keep this really light (admin/kickstart)
```

PIL
==========

Python imaging library needs to be built on Ubuntu 12.04 64bit and it's messy
Here are the essentials (Paths may vary depending on architecture etc.)
```
# apt-get install python-dev
# apt-get install libjpeg8 libpng12-0 libfreetype6 zlib1g
# apt-get install python-imaging
# ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
# ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
pip install -U PIL

```

Postgresql
==========

I like to use postgresql for development so this is something worth keeping handy (close but not this close)

Install at lease 9.2 (has some functionality I would like to explore)
```
# add-apt-repository ppa:pitti/postgresql
# apt-get update
# apt-get install postgresql-9.2
```
Configure postgresql for remote access (valid for ubunto and my network):
```
# su postgres

vim /etc/postgresql/9.2/main/postgresql.conf
* listen_addresses = '*'

vim /etc/postgresql/9.2/main/pg_hba.conf
host all all 192.168.1.0/24 trust

/etc/init.d/postgresql restart

```