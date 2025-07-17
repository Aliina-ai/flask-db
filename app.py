from flask import Flask, request, render_template
import psycopg2
import os

app = Flask(__name__)
DATABASE_URL = os.environ.get('DATABASE_URL')

def get_conn():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS entries (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL
                   )''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_conn()
    cur = conn.cursor()
    if request.method == 'POST':
        content = request.form['content']
        cur.execute("INSERT INTO entries (content) VALUES (%s)", (content,))
        conn.commit()
    cur.execute("SELECT * FROM entries")
    entries = cur.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
