from flask import Flask, render_template, request, url_for, redirect, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DB_PATH = os.getenv("DB_PATH", "/data/db.sqlite")

USERS = {
    'Аліна':     {'password': 'Gk47fBq2', 'role': 'admin'},
    'Наталія':   {'password': 'qF92KsLm', 'role': 'admin'},
    'Сергій':    {'password': 'xP74gVt1', 'role': 'operator'},
    'Геннадій':  {'password': 'zT38mWc9', 'role': 'operator'},
}


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

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

        c.execute('''
            CREATE TABLE IF NOT EXISTS regions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                large_okrug TEXT,
                district_name TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                address TEXT,
                phone TEXT,
                birth_date TEXT,
                location TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS activists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                large_okrug TEXT,
                okrug TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                address TEXT,
                phone TEXT,
                birth_date TEXT,
                subscribers_count INTEGER,
                newspapers_count INTEGER,
                location TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS subscribers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                okrug INTEGER,
                polling_station TEXT,
                last_name TEXT,
                first_name TEXT,
                middle_name TEXT,
                street TEXT,
                building TEXT,
                apartment TEXT,
                phone TEXT,
                activist TEXT
            )
        ''')

        conn.commit()


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


# ---------- REGIONS LARGE ----------
@app.route('/regions-large')
def regions_large():
    if 'username' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM regions_large")
        rows = c.fetchall()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'last_name': row[2],
        'first_name': row[3],
        'middle_name': row[4],
        'phone': row[5],
        'location': row[6]
    } for row in rows]

    return render_template('regions_large.html', data=data)


@app.route('/add-region-large', methods=['GET', 'POST'])
def add_region_large():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати записи.')
        return redirect(url_for('regions_large'))

    if request.method == 'POST':
        locations = request.form.getlist('location')
        location_str = ', '.join(locations)

        with sqlite3.connect(DB_PATH) as conn:
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
                location_str
            ))
            conn.commit()
        return redirect(url_for('regions_large'))

    return render_template('add_region_large.html')


@app.route('/regions-large/edit/<int:region_id>', methods=['GET', 'POST'])
def edit_region_large(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати записи.')
        return redirect(url_for('regions_large'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        if request.method == 'POST':
            locations = request.form.getlist('location')
            location_str = ', '.join(locations)

            c.execute('''
                UPDATE regions_large SET
                    okrug = ?, last_name = ?, first_name = ?, middle_name = ?, phone = ?, location = ?
                WHERE id = ?
            ''', (
                request.form['okrug'],
                request.form['last_name'],
                request.form['first_name'],
                request.form['middle_name'],
                request.form['phone'],
                location_str,
                region_id
            ))
            conn.commit()
            return redirect(url_for('regions_large'))

        c.execute('SELECT * FROM regions_large WHERE id = ?', (region_id,))
        row = c.fetchone()

    if not row:
        flash('Запис не знайдено.')
        return redirect(url_for('regions_large'))

    region = {
        'okrug': row[1],
        'last_name': row[2],
        'first_name': row[3],
        'middle_name': row[4],
        'phone': row[5],
        'location': row[6].split(', ') if row[6] else []
    }

    return render_template('add_region_large.html', edit=True, region=region)


@app.route('/regions-large/delete/<int:region_id>', methods=['POST'])
def delete_region_large(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти записи.')
        return redirect(url_for('regions_large'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM regions_large WHERE id = ?', (region_id,))
        conn.commit()

    flash('Запис успішно видалено.')
    return redirect(url_for('regions_large'))


# ---------- REGIONS ----------
@app.route('/regions')
def regions():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM regions")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0], 'large_okrug': row[1], 'district_name': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'address': row[6], 'phone': row[7], 'birth_date': row[8], 'location': row[9]
    } for row in rows]

    return render_template('regions.html', data=data)


@app.route('/regions/add', methods=['GET', 'POST'])
def add_region():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Недостатньо прав')
        return redirect(url_for('regions'))

    if request.method == 'POST':
        num = int(request.form['okrug_num'])
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO regions (
                large_okrug, district_name, last_name, first_name, middle_name,
                address, phone, birth_date, location
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            ((num - 1) // 7 + 1),
            num,
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birthday'],
            request.form['location']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('regions'))

    return render_template('add_edit_region.html', edit=False)


@app.route('/regions/edit/<int:region_id>', methods=['GET', 'POST'])
def edit_region(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('regions'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        loc = ', '.join(request.form.getlist('location'))
        c.execute('''
            UPDATE regions SET large_okrug=?, district_name=?, last_name=?, first_name=?,
                middle_name=?, address=?, phone=?, birth_date=?, location=?
            WHERE id=?
        ''', (
            request.form['large_okrug'],
            request.form['district_name'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            loc,
            region_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('regions'))

    c.execute('SELECT * FROM regions WHERE id=?', (region_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        flash('Не знайдено.')
        return redirect(url_for('regions'))

    region = {
        'id': row[0], 'large_okrug': row[1], 'district_name': row[2],
        'last_name': row[3], 'first_name': row[4], 'middle_name': row[5],
        'address': row[6], 'phone': row[7], 'birth_date': row[8], 'location': row[9].split(', ')
    }

    return render_template('add_region.html', edit=True, region=region)


@app.route('/regions/delete/<int:region_id>', methods=['POST'])
def delete_region(region_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('regions'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM regions WHERE id = ?', (region_id,))
    conn.commit()
    conn.close()
    flash('Видалено.')
    return redirect(url_for('regions'))


# ---------- ACTIVISTS ----------
@app.route('/activists')
def activists():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM activists")
    rows = c.fetchall()
    conn.close()

    data = [{
        'id': row[0],
        'large_okrug': row[1],
        'okrug': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'address': row[6],
        'phone': row[7],
        'birth_date': row[8],
        'subscribers_count': row[9],
        'newspapers_count': row[10],
        'location': row[11]
    } for row in rows]

    return render_template('activists.html', data=data)


@app.route('/activists/add', methods=['GET', 'POST'])
def add_activist():
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може додавати.')
        return redirect(url_for('activists'))

    if request.method == 'POST':
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO activists (
                large_okrug, okrug, last_name, first_name, middle_name,
                address, phone, birth_date, subscribers_count,
                newspapers_count, location
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            request.form['large_okrug'],
            request.form['okrug'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            request.form['subscribers_count'],
            request.form['newspapers_count'],
            request.form['location']
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('activists'))

    return render_template('add_activist.html')


@app.route('/activists/edit/<int:activist_id>', methods=['GET', 'POST'])
def edit_activist(activist_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('activists'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    if request.method == 'POST':
        c.execute('''
            UPDATE activists SET
                large_okrug = ?, okrug = ?, last_name = ?, first_name = ?,
                middle_name = ?, address = ?, phone = ?, birth_date = ?,
                subscribers_count = ?, newspapers_count = ?, location = ?
            WHERE id = ?
        ''', (
            request.form['large_okrug'],
            request.form['okrug'],
            request.form['last_name'],
            request.form['first_name'],
            request.form['middle_name'],
            request.form['address'],
            request.form['phone'],
            request.form['birth_date'],
            request.form['subscribers_count'],
            request.form['newspapers_count'],
            request.form['location'],
            activist_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('activists'))

    c.execute('SELECT * FROM activists WHERE id = ?', (activist_id,))
    row = c.fetchone()
    conn.close()

    if not row:
        flash('Активіста не знайдено.')
        return redirect(url_for('activists'))

    activist = {
        'id': row[0],
        'large_okrug': row[1],
        'okrug': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'address': row[6],
        'phone': row[7],
        'birth_date': row[8],
        'subscribers_count': row[9],
        'newspapers_count': row[10],
        'location': row[11]
    }

    return render_template('add_activist.html', edit=True, activist=activist)


@app.route('/activists/delete/<int:activist_id>', methods=['POST'])
def delete_activist(activist_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може видаляти.')
        return redirect(url_for('activists'))

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM activists WHERE id = ?', (activist_id,))
    conn.commit()
    conn.close()
    flash('Запис успішно видалено.')
    return redirect(url_for('activists'))

# ---------- SUBSCRIBERS ----------
@app.route('/subscribers')
def subscribers_home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('subscribers_home.html')


def render_okrug_subscribers(okrug_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM subscribers WHERE okrug = ?", (okrug_id,))
        rows = c.fetchall()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'polling_station': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'street': row[6],
        'building': row[7],
        'apartment': row[8],
        'phone': row[9],
        'activist': row[10]
    } for row in rows]

    return render_template('regions_generic.html', data=data, okrug_id=okrug_id)

@app.route('/regions1')
def regions1():
    return render_okrug_subscribers(1)

@app.route('/add_edit_subscriber1.html', methods=['GET', 'POST'])
def add_edit_subscriber1():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Визначаємо перелік будинків для округу 1
    buildings = list(range(1, 5)) + [5, 6] + ["77/43"] + list(range(131)) + list(range(139, 178)) + \
                [180, 181, 182, 183, 184, 185] + [214, 215] + list(range(219, 228)) + \
                list(range(228, 271)) + [399, 400, 401, 402, 403]

    # Отримуємо унікальних активістів округу 1
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT DISTINCT last_name || ' ' || first_name || ' ' || middle_name FROM activists WHERE okrug = 1")
    activists = [row[0] for row in c.fetchall()]
    conn.close()

    if request.method == 'POST':
        okrug = 1
        polling_station = request.form['polling_station']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        street = request.form['street']
        building = request.form['building']
        apartment = request.form['apartment']
        phone = request.form['phone']
        activist = request.form['activist']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO subscribers (
                okrug, polling_station, last_name, first_name, middle_name,
                street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            okrug, polling_station, last_name, first_name, middle_name,
            street, building, apartment, phone, activist
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('regions1'))  # Повернення до перегляду округу

    return render_template(
    'add_subscriber1.html',
    buildings=sorted(set(buildings), key=lambda x: str(x)),
    activists=activists
)

@app.route('/regions2')
def regions2():
    if 'username' not in session:
        return redirect(url_for('login'))

    okrug_id = 2
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM subscribers WHERE okrug = ?", (okrug_id,))
        rows = c.fetchall()

    data = [{
        'id': row[0],
        'okrug': row[1],
        'polling_station': row[2],
        'last_name': row[3],
        'first_name': row[4],
        'middle_name': row[5],
        'street': row[6],
        'building': row[7],
        'apartment': row[8],
        'phone': row[9],
        'activist': row[10]
    } for row in rows]

    return render_template('regions_generic.html', data=data, okrug_id=okrug_id, okrug=okrug_id)

@app.route('/subscribers1/edit/<int:subscriber_id>', methods=['GET', 'POST'])
def edit_subscriber1(subscriber_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Лише адміністратор може редагувати.')
        return redirect(url_for('regions1'))

    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()

        if request.method == 'POST':
            c.execute('''
                UPDATE subscribers SET
                    polling_station=?, last_name=?, first_name=?, middle_name=?,
                    street=?, building=?, apartment=?, phone=?, activist=?
                WHERE id=?
            ''', (
                request.form['polling_station'],
                request.form['last_name'],
                request.form['first_name'],
                request.form['middle_name'],
                request.form['street'],
                request.form['building'],
                request.form['apartment'],
                request.form['phone'],
                request.form['activist'],
                subscriber_id
            ))
            conn.commit()
            return redirect(url_for('regions1'))

        c.execute("SELECT * FROM subscribers WHERE id = ?", (subscriber_id,))
        row = c.fetchone()

    if not row:
        flash("Підписника не знайдено.")
        return redirect(url_for('regions1'))

    # Повторно отримаємо активістів
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT DISTINCT last_name || ' ' || first_name || ' ' || middle_name FROM activists WHERE okrug = 1")
        activists = [r[0] for r in c.fetchall()]

    buildings = (
        list(range(1, 5)) + [5, 6, "77/43"] +
        list(range(89, 131)) + list(range(139, 178)) +
        [180, 181, 182, 183, 184, 185, 214, 215] +
        list(range(219, 228)) + list(range(228, 271)) +
        [399, 400, 401, 402, 403]
    )

    subscriber = {
        'id': row[0], 'polling_station': row[2], 'last_name': row[3],
        'first_name': row[4], 'middle_name': row[5], 'street': row[6],
        'building': row[7], 'apartment': row[8], 'phone': row[9],
        'activist': row[10]
    }

    return render_template(
        'add_edit_subscriber1.html',
         edit=False,
         okrug_id=1,
         buildings=sorted(set(buildings), key=lambda x: str(x)),
         activists=activists
     )



@app.route('/subscribers/delete/<int:sub_id>', methods=['POST'])
def delete_subscriber(sub_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('Недостатньо прав для видалення.')
        return redirect(url_for('subscribers_home'))
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM subscribers WHERE id = ?", (sub_id,))
        conn.commit()
    flash('Підписника успішно видалено.')
    # Повертаємося до відповідного округу
    # Якщо знаєте округ, можете редіректити: `url_for('regions1')` або загальний `subscribers_home`
    return redirect(request.referrer or url_for('subscribers_home'))

@app.route('/add_subscriber2', methods=['GET', 'POST'])
def add_subscriber2():
    if 'username' not in session:
        return redirect(url_for('login'))

    buildings_map = {
        'Волонтерська': {
            '321100': list(range(12, 30)),
            '321102': [1, '1А', 3, 9]
        },
        'Івана Пулюя': {
            '321100': list(range(1, 31)) + ['32', '32А']
        },
        'Січневого прориву': {
            '321100': [29, 31, 35] + ['43', '43Б', '45', '45А'] +
                      [47, '49', '49А', 51, 53, 55, 57, 59, 61]
        },
        'Сквирське шосе': {
            '321102': list(range(221, 224)) + list(range(228, 267))
        }
    }

    all_buildings = sorted({str(b) for addr in buildings_map.values() for b_list in addr.values() for b in b_list})
    all_streets = list(buildings_map.keys())

    # Отримуємо список активістів округу 2
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT DISTINCT last_name || ' ' || first_name || ' ' || middle_name FROM activists WHERE okrug = 2")
    activists = [row[0] for row in c.fetchall()]
    conn.close()

    if request.method == 'POST':
        okrug = 2
        street = request.form['street']
        building = request.form['building']

        polling_station = ''
        for ps, b_list in buildings_map.get(street, {}).items():
            if building in map(str, b_list):
                polling_station = ps
                break

        last_name = request.form['last_name']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        apartment = request.form['apartment']
        phone = request.form['phone']
        activist = request.form['activist']

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO subscribers (
                okrug, polling_station, last_name, first_name, middle_name,
                street, building, apartment, phone, activist
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            okrug, polling_station, last_name, first_name, middle_name,
            street, building, apartment, phone, activist
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('regions2'))

    return render_template(
        'add_subscriber2.html',
        streets=all_streets,
        buildings=all_buildings,
        activists=activists
    )


# ---------- APP LAUNCH ----------
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

