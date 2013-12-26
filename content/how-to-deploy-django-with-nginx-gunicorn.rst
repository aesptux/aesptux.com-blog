How to deploy django with nginx + gunicorn
##########################################
:date: 2012-10-23 21:43
:author: aesptux
:category: Django, Linux, Python
:tags: centos, deploy, django, fedora, gunicorn, nginx, python
:slug: how-to-deploy-django-with-nginx-gunicorn

Django is a great web framework and we have several ways to deploy it in
production.

You can use apache too for example, but for django my favorite is nginx
+ gunicorn.

Nginx is a well-known player and it will be used as front-end. Gunicorn
is not as well-known, but it has proved to be quite stable (instagram
and pinterest use it).

Installation:

::

    yum install nginx
    pip install gunicorn

Previously you have to have installed python pip and epel repository.

Next step is to run gunicorn, which is quite easy. As we are going to
run it with a django project, it is possible to use *gunicorn\_django *

::

    cd /path/to/your/django/project
    gunicorn_django --workers=4 -b 127.0.0.1:8888 -D

And that is it. We have told gunicorn to run with 4 workers (processes),
to listen on localhost:8888 and to run in background with -D.

Last step is to configure a server for nginx:

::

    upstream app_server_djangoapp {
        server localhost:8888 fail_timeout=0;
    }

    server {
            listen 80;
            server_name  server.com;

            access_log  /path/log/access.log;
            error_log  /path/log/error.log info;

        keepalive_timeout 5;

        # path for static folder
        location /static {
            root /path/to/static/;
        }
        location / {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header Host $http_host;
            proxy_redirect off;

            if (!-f $request_filename) {
                proxy_pass http://app_server_djangoapp;
                break;
            }
        }
    }

Restart nginx:

::

    service nginx restart

Our django site is deployed, as easy as that.
