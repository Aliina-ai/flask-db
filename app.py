from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_conn():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO responses (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        conn.close()
        return 'Дякуємо за відповідь!'
    return render_template('form.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
