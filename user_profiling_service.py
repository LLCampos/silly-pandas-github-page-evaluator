from flask import Flask, request, redirect, url_for, render_template, flash
#from flask_login import login_user, logout_user, current_user, login_required, LoginManager
import os
from User import User
#import models

import github3


# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True
SECRET_KEY = 'secret_key'

# create app
app = Flask(__name__)
app.config.from_object(__name__)

gh = github3.GitHub()

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def profile_user():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        user = User(username)
        return render_template('profile.html', user=user)





if __name__ == '__main__':
    app.run()
