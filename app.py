from flask import Flask, render_template, request, redirect, session, flash
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
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'operator'))
        )
    ''')

    users = [
        ('alina', 'Alina#2024@adm', 'admin'),
        ('natalia', 'Natalia!2024#adm', 'admin'),
        ('gennadiy', 'Gennadiy_2024$op', 'operator'),
        ('sergiy', 'Sergiy-2024@op', 'operator'),
    ]

    for login, password, role in users:
        c.execute('''
            INSERT INTO users (login, password, role)
            VALUES (?, ?, ?)
            ON CONFLICT(login) DO UPDATE SET
            password=excluded.password,
            role=excluded.role
        ''', (login, password, role))

    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login'].strip().lower()
        password = request.form['password']
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE login = ? AND password = ?', (login, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = user[1]
            session['role'] = user[3]
            return redirect('/dashboard')
        else:
            flash("Невірний логін або пароль")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return f"<h1>Вітаємо, {session['user']}!</h1><p>Ваша роль: <b>{session['role']}</b></p>"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
