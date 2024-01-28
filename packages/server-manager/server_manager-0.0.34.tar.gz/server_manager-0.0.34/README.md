# Server manager
is a simple server monitoring web dashboard with a couple of management features.

## Installation
### With pip

```commandline
pip install server-manager
```

### Build from source

```commandline
git clone https://gitlab.com/serverman-group/serverman
cd serverman
python -m build
pip install .
```

## Running the dashboard
To run the dashboard you have to use gunicorn (installed as a dependency)

run syntax:
```commandline
python -m gunicorn -b host:port server-manager.wsgi:app
```

if you have gunicorn installed as a system-wide package you can simply use ``gunicorn`` removing ``python -m`` 

run command example:
```commandline
python -m gunicorn -b 0.0.0.0:8080 server-manager.wsgi:app
```

### Explanation

``python -m`` runs a python package, in this case ``gunicorn``, the ``-b`` flag specifies bind, ``--bind can also be used``
, this binds the ``wsgi`` server to a certain host and port, in this case ``0.0.0.0`` and port ``8080``.

The host ``0.0.0.0`` is used so the server can be accessible network wide.
The port really can be specified to anything except ports like ``80`` or ``443``, that require escalated
privileges. For the server to be accessible on port ``80`` or ``443`` both the [flask](https://flask.palletsprojects.com/en/3.0.x/) and [gunicorn](https://gunicorn.org/#docs) documentations
recommend using a reverse proxy like [apache httpd](https://www.apache.org/) and [nginx](https://www.nginx.com/).

### Accessing the webpage
To see the webpage simply go to ip address of the device the dashboard is running on.<br>
example: ``localhost:8080`` or ``192.168.xx.xx:8080``. If you are using a reverse proxy setup as mentioned before
you can access the dashboard from the reverse proxy server ip and port (this can be the same machine running the dashboard)
, make sure that if the reverse proxy server and the dashboard are running on the same machine, they are not running on the same port.

Once you open the webpage you will see this:<br>
![Home screen view](markdown-assets/startpage.png)<br>

This is the start page of the serverman dashboard.
Once you navigate to one of the links you will be prompted to log in:<br>

![login page](markdown-assets/login.png)<br>
In this login page you are required to log in as one of the system users with their username and password
to proceed with the server's monitoring and management.

After the login the links do not redirect you to login anymore and you can start monitoring. The login system
is session based and made with flask-login.

This app features a
1. dashboard
2. settings
3. process management

page.

## Short description for each page

### Dashboard

The dashboard page provides the ability to view system metrics like cpu clock speed, memory and swap usage.
<br>
#### Systime block
![systime](markdown-assets/systime.jpg)<br>



### Dashboard settings
The dashboard settings page or just ``settings``
allows you to make simple adjustments to what the dashboard page displays.
The page also allows the the interval at witch the information to be updated.
This can really help lower end systems like older raspberry pi's.

### Processes

The processes tab shows the currently running processes and also kill them.

The update interval of the processes table can also be adjusted in the settings page.


