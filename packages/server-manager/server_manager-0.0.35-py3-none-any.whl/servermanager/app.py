from flask import Flask, render_template, send_from_directory, send_file, request, redirect, url_for, flash
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import servermanager.info as info
import servermanager.graph as graph
from threading import Thread
from flask_cors import CORS
import json
import servermanager.auth as auth
import os
import subprocess
import signal
import pkg_resources


preceeder = ""

users = auth.readable_valid_user_data
user_instances = []

filepath = pkg_resources.resource_filename(__name__, 'settings/settings.json')
cfgj = open(filepath).read()


class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.username = username 
        self.password = password
        self.user_id = user_id

    def get_id(self):
        return self.user_id


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


app = Flask(__name__)
app.config.update(SECRET_KEY=os.popen('echo $FLASK_SECRET_KEY').read())
CORS(app)

Thread(target=graph.always_gen).start()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = preceeder + '/login'


@login_manager.user_loader
def load_user(user_id):
    for i in user_instances:
        if i.user_id == user_id:
            return i
  

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data

        for i in users:
            if i['username'] == username:
                user_id = i['user_id']
                break

        try:
          user = User(user_id, form.username.data, form.password.data)
        except:
          #prin("user not found")
          return render_template('login.html', form=form, pre=preceeder)

        output = auth.authenticate(username, password, "echo 'Success'")

        if b'Success' in output:
          login_user(user)
          user_instances.append(user)
          next_page = request.args.get('next', "home")
          return redirect(preceeder + url_for(next_page))

    else:
        return render_template('login.html', form=form, pre=preceeder)


@app.route('/')
def home():
    return render_template('index.html', pre=preceeder)


@app.route('/kill', methods=['POST'])
@login_required
def kill():
    print(int(list(dict(request.form).keys())[0].split(':')[1]))
    os.kill(int(list(dict(request.form).keys())[0].split(':')[1]), signal.SIGINT)
    return redirect(preceeder + url_for('proc'))


@app.route('/dashboard')
@login_required
def dashboard():
  static_sysinfo = info.system_static()
  dynamic_sysinfo = info.system_dynamic()
  cfgj = open(filepath).read()
  config = json.loads(open(filepath).read())
  return render_template('dashboard.html', cfgj=cfgj, static_sysinfo=static_sysinfo, dynamic_sysinfo=dynamic_sysinfo, config=config, pre=preceeder)


@app.route('/scripts/<scriptname>')
def frontend_script(scriptname):
  #return send_from_directory('frontend_code', 'script.js')
  return send_file(f'scripts/{scriptname}')


@app.route('/styles/style.css')
def frontend_style():
  #return send_from_directory('frontend_code', 'style.css')
  return send_file('styles/style.css')


@app.route('/graphs/cpu_usage_1')
def cpu_usage_1():
  return send_file('graphs/cpu_usage_1.svg')


@app.route('/graphs/memory_usage_1')
def memory_usage_1():
  return send_file('graphs/memory_usage_1.svg')


@app.route('/ddata')
@login_required
def ddata():
  return info.system_dynamic().get_json()


@app.route('/sdata')
@login_required
def sdata():
  return info.system_static().get_json()


@app.route('/dashboard_settings')
@login_required
def settings():
  config = json.loads(open(filepath).read())
  return render_template('settings.html', config=config, pre=preceeder, type=type, cfgj=cfgj, str=str)


@app.route('/settings/<settingname>')
@login_required
def profile(settingname):
  return open(f'settings/{settingname}.json')


@app.route('/proc', methods=['GET'])
@login_required
def proc():
  proc = info.proc()
  return render_template('processes.html', proc=proc, pre=preceeder, lenght=len(proc.keys()), config=open(filepath).read())


@app.route('/processes', methods=['GET'])
@login_required
def processes():
  data = info.proc()
  return json.dumps(data)


@app.route('/settings/save', methods=['POST'])
@login_required
def update():
  form = dict(request.form)
  #config = json.loads(open('settings/settings.json').read())
  #prin(form)

  settings = json.loads(open(filepath).read())

  for i in settings['show'].keys():
    settings['show'][i] = False
  
  for i in form.keys():
    if form[i] == 'on':
      settings['show'][i] = True
    if "interval" in i:
      settings['interval'].update({i: float(form[i]) * 1000})
  #for i in form.keys():
    #form[i] = True

  #for j in config.keys():
    #config[j] = False

  #for k in form.keys():
    #config[k] = form[k]

  #prin(form)
  #print(config)
  f = open(filepath, 'w')
  f.write(json.dumps(settings))
  f.close()
  return redirect(preceeder + url_for('dashboard'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

