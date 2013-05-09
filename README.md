Django-SPDY
===========
The main goal of this experimental project is to deliver **Django 1.4.5** web pages using Jetty web container.
The usefulness of this is to use Jetty SPDY support together with the capabilities to push associated resources of a main request (SPDY push). If you want further information, [there is an article][9] about this experiment.

Django-SPDY up and running
==========================
To achieve this integration and build war package it's necessary to use [Jython][1] interpreter with [django-jython][2] app.
Follow these step if you want to be up and running with this experiment!

Prerequisite
------------
* OpenJDK 7
* [Jython 2.5.3][5]
* [Jetty 8 stable][6]
* [Next Protocol Negotiation (NPN)][7] JAR library
* A browser that supports SPDY/2 or SPDY/3

**Note:** NPN implementation relies on modifications of OpenJDK classes so you need to use the correct version according to your JDK version. You can find a list of the correct NPN library [here][8].
NPN library can be put on your `$JETTY_HOME`.

Virtualenv configuration
------------------------
Virtualenv must be created using `jython` interpreter as follows (be sure that jython interpreter is in your `$PATH`):

    $ mkvirtualenv django-spdy -p jython
    $ workon django-spdy
    $ pip install -r requirements.txt

Build war package
-----------------
Be sure that `'doj'` is enabled on Django `INSTALLED_APPS`. Then use:

    $ jython manage.py war

Jetty configuration
-------------------
First you must configure your `$JETTY_HOME/start.ini` to enable a customized XML configuration and SPDY support. Edit this line:

    OPTIONS=Server,spdy

and also be sure that in `Configuration files` section these elements are enabled:

    etc/jetty.xml
    etc/jetty-deploy.xml
    etc/jetty-webapps.xml
    etc/jetty-spdy-push.xml

Jetty SPDY push configuration file
----------------------------------
To have SPDY up and running you should provide `jetty-spdy-push.xml` that is available in download section of this repository. Feel free to use it as a basic configuration for this experiment.

And now?
--------
Deploy your Django app (`django_spdy.war`) inside Jetty webapps folder (`$JETTY_HOME/webapps/root.war`).
Now you can run jetty:

    $ java -Xbootclasspath/p:npn-boot-{YOUR_NPN_VERSION}.jar -jar start.jar

**Ready to push?**

* http://localhost:8080 (HTTP)
* https://localhost:8443 (SPDY without push strategy)
* https://localhost:8444 (SPDY with push strategy)

Pre-build package and configuration
===================================
* A **war package** is available in downloads section
* All Jetty SPDY push **configuration files** are available in downloads section

[1]: http://jython.org/
[2]: http://code.google.com/p/django-jython/
[3]: http://spdy.evonove.it
[4]: https://spdy.evonove.it
[5]: http://jython.org/downloads.html
[6]: http://download.eclipse.org/jetty/
[7]: http://wiki.eclipse.org/Jetty/Feature/NPN
[8]: http://www.eclipse.org/jetty/documentation/current/npn-chapter.html#npn-versions
