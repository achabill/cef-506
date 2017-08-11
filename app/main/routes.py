from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm

users = []
rooms = ['public']


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()

    if request.method == 'POST':
        name = request.form['name']
        if name in users:
            return render_template('index.html', error="Username already taken")
        users.append(name)
        session['users'] = users
        session['rooms'] = rooms

        return redirect(url_for('.home'))
    return render_template('index.html', form=form)


@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
