django-kickstart
================

An attempt to create a private django kickstart, please view this as "learn by doing" exercise rather than a viable option for anyone other than me.

Included packages

* docutils - just to get the django documentation working

* django-crispy-forms - for better form handling and twitter-bootstrap compatibility
    * https://github.com/maraujop/django-crispy-forms
    * http://django-crispy-forms.readthedocs.org/en/d-0/install.html#installing-django-crispy-forms

* django-tastypie - for all the REST API goodies
    * https://github.com/toastdriven/django-tastypie

* django-grapelli - Seem to be back on track with their fine admin UI enhancement
    * https://github.com/sehmaschine/django-grappelli
    * http://django-grappelli.readthedocs.org/en/2.4.2/index.html

* django-filebrowser - for admin filebrowsing in grappelli
    * https://github.com/sehmaschine/django-filebrowser
    * http://django-filebrowser.readthedocs.org/en/latest/

* python-memcached - Caching backend for the Django caching framework
    * http://www.tummy.com/Community/software/python-memcached/

* django-devserver - for complete debugging
    * https://github.com/dcramer/django-devserver
    * Reccomended packages:
        * pip install sqlparse
        * pip install werkzeug
        * pip install guppy #Not working correctly on my ubuntu 12.04 system (not looked into it)
        * pip install line_profiler

* django-debug-toolbar - for some in-page-debugging
    * https://github.com/dcramer/django-debug-toolbar

* django-extensions - admin utilities (and model documentation tools)
    * http://packages.python.org/django-extensions
    * # apt-get install libgraphviz-dev
    * pip install pygraphviz

* django-waffle - feature flipping is nice to have when moving fast
    * https://github.com/jsocol/django-waffle
    * http://waffle.readthedocs.org/en/latest/index.html

* raven - Sentry client for better exception logging
    * pip install raven
    * https://www.getsentry.com/docs/python/django/

* sorl-thumbnail - Thumbnail creation and management
    * https://github.com/sorl/sorl-thumbnail
    * http://sorl-thumbnail.readthedocs.org

* django-appconf - Simple app configuration framework
    * http://django-appconf.readthedocs.org
    * https://github.com/jezdez/django-appconf/

* requests  - HTTP communications library
    * pip install requests

* lxml      - xml manipulation
    * pip install lxml


Other requirements

Sqlite3
=======
Only if you want to keep this really light (admin/kickstart)
```
# sudo apt-get install sqlite3
```

PIL
===

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