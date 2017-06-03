from flask import Flask, request, render_template
import os
from User import User


# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True
SECRET_KEY = 'secret_key'

# create app
app = Flask(__name__)
app.config.from_object(__name__)


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
