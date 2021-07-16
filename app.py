# import the Flask class from flask module
from flask import Flask, render_template, redirect, \
     url_for, request, session, flash, g
from functools import wraps
import sqlite3

# create the application object
app = Flask(__name__)

# config 
app.secret_key = 'my precious'
app.database = "sample.db"

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# use decorators to link the function to an URL
@app.route('/')
@login_required
def home():
    # return render_template('about.html') # render a template      
    # return "Good morning worldzz" # return some string
    # posts
    # g.db = connect_db()
    # cur = g.db.execute('select * from posts')
    # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    # g.db.close()

    # squash players
    g.db = connect_db()
    cur = g.db.execute('select * from players')
    players = [dict(playerid=row[0], playername=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', players = players)

@app.route('/welcome')   
@login_required 
def welcome():
    return render_template('index.html')
    # return render_template('welcome.html') # render a template

@app.route('/about')   
@login_required 
def about():
    return render_template('about.html') # render a template        

# Route for handling the login page logic
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password']!= 'admin':
            error = 'Invalid credentials. Please try again!'
        else:
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('welcome'))

# connect to database
def connect_db():
    return sqlite3.connect(app.database)

# start server with the 'run()' method
if __name__ == '__main__':
    app.run(debug = True)