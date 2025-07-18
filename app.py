from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.getenv("DB_PATH", "data/db.sqlite")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if request.method == 'POST':
        content = request.form['content']
        c.execute("INSERT INTO entries (content) VALUES (?)", (content,))
        conn.commit()
    c.execute("SELECT * FROM entries")
    entries = c.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
    
