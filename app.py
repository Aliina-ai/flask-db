from flask import Flask, render_template, request, url_for, redirect, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_PATH = os.getenv("DB_PATH", "/data/db.sqlite")

# Користувачі
USERS = {
    'Аліна':     {'password': 'Gk47fBq2', 'role': 'admin'},
    'Наталія':   {'password': 'qF92KsLm', 'role': 'admin'},
    'Сергій':    {'password': 'xP74gVt1', 'role': 'operator'},
    'Геннадій':  {'password': 'zT38mWc9', 'role': 'operator'},
}

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Таблиця entries (залишаю, якщо ти її ще використовуєш)
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    ''')

    # Таблиця regions_large
    c.execute('''
        CREATE TABLE IF NOT EXISTS regions_large (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            okrug TEXT,
            last_name TEXT,
            first_name TEXT,
            middle_name TEXT,
            phone TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = USERS.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            error = 'Невірне ім’я або пароль'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'], role=session['role'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/regions-large')
def regions_large():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions_large")
    rows = c.fetchall()
    conn.close()

    data = [
        {
            'okrug': row[1],
            'last_name': row[2],
            'first_name': row[3],
            'middle_name': row[4],
            'phone': row[5],
            'location': row[6]
        }
        for row in rows
    ]
    return render_template('regions_large.html', data=data)

@app.route('/add-region-large', methods=['POST'])
def add_region_large():
    if 'username' not in session:
        return redirect(url_for('login'))
    if session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('regions_large'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO regions_large (okrug, last_name, first_name, middle_name, phone, location)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        request.form['okrug'],
        request.form['last_name'],
        request.form['first_name'],
        request.form['middle_name'],
        request.form['phone'],
        request.form['location']
    ))
    conn.commit()
    conn.close()
    return redirect(url_for('regions_large'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

