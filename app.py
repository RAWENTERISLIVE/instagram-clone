from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import create_connection
import hashlib
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages and sessions

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = hash_password(request.form['password'])
    
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
                         (username, password))
            user = cursor.fetchone()
            
            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Successfully logged in!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for('login'))
        except Error as e:
            flash('An error occurred', 'error')
            return redirect(url_for('login'))
        finally:
            conn.close()
    
    flash('Database connection error', 'error')
    return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    fullname = request.form['fullname']
    username = request.form['username']
    password = hash_password(request.form['password'])
    
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, fullname, password)
                VALUES (?, ?, ?, ?)
            ''', (username, email, fullname, password))
            
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists', 'error')
            return redirect(url_for('signup'))
        except Error as e:
            flash('An error occurred', 'error')
            return redirect(url_for('signup'))
        finally:
            conn.close()
    
    flash('Database connection error', 'error')
    return redirect(url_for('signup'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)
