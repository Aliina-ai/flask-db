from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_PATH = os.getenv("DB_PATH", "/data/auth.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    # Створюємо тестового користувача (логін: admin, пароль: admin)
    c.execute('SELECT * FROM users WHERE login = ?', ('admin',))
    if not c.fetchone():
        c.execute('INSERT INTO users (login, password) VALUES (?, ?)', ('admin', 'admin'))
        conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = login
            return redirect('/dashboard')
        else:
            flash('Невірний логін або пароль')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return f"<h1>Ласкаво просимо, {session['user']}</h1>"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)



    
