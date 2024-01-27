# Server manager
is a simple server monitoring web dashboard with a couple of management features.

## Installation
You can install server manager from pip:

```commandline
$ pip install server-manager
```

## Running the dashboard
To run the dashboard you have to use gunicorn (installed as a dependency)

run syntax:
```commandline
$ python -m gunicorn -b host:port serverman.wsgi:app
```

if you have gunicorn installed as a system-wide package you can simply use ``gunicorn`` removing ``python -m`` 

run command example:
```commandline
$ python -m gunicorn -b 0.0.0.0:8080 serverman.wsgi:app
```

### Explanation

``python -m`` runs a python package, in this case ``gunicorn``, the ``-b`` flag specifies bind, ``--bind can also be used``
, this binds the ``wsgi`` server to a certain server and port, in this case ``0.0.0.0`` and port ``8080``.

The host ``0.0.0.0`` is used so the server can be accessible network wide.
The port really can be specified to anything except ports like ``80`` or ``443``, that require escalated
privileges. For the server to be accessible on port ``80`` or ``443`` both the [flask](https://flask.palletsprojects.com/en/3.0.x/) and [gunicorn](https://gunicorn.org/#docs) documentations
recommend using a reverse proxy like [apache httpd](https://www.apache.org/) and [nginx](https://www.nginx.com/).