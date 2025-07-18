from flask import Flask, render_template, request, redirect, session, url_for
from users import users
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 🔐 Заміни на свій

big_data = []
small_data = []
elders_data = []

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            error = "Невірний логін або пароль"

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

@app.route('/big_list')
def big_list():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('big_list.html', data=big_data)

@app.route('/add_big', methods=['GET', 'POST'])
def add_big():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        district = request.form.get('district_number')
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        phone = request.form.get('phone')
        pickup_points = request.form.get('pickup_points')  # рядок з локаціями

        big_data.append({
            'district_number': district,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'phone': phone,
            'pickup_points': pickup_points
        })

        return redirect(url_for('big_list'))  # після збереження — назад у таблицю

    return render_template('add_big.html')

# Сторінка зі списком анкет малих округів
@app.route('/small_list')
def small_list():
    return render_template('small_list.html', small_data=small_data)

# Додавання нової анкети
@app.route('/add_small', methods=['GET', 'POST'])
def add_small():
    if request.method == 'POST':
        district = int(request.form['district'])

        # Автоматичне визначення великого округу
        if 1 <= district <= 7:
            big_district = 1
        elif 8 <= district <= 14:
            big_district = 2
        elif 15 <= district <= 19:
            big_district = 3
        elif 20 <= district <= 28:
            big_district = 4
        elif 29 <= district <= 35:
            big_district = 5
        elif 36 <= district <= 42:
            big_district = 6
        else:
            big_district = "Невідомо"

        # Створюємо словник анкети
        new_entry = {
            'big_district': big_district,
            'district': district,
            'last_name': request.form['last_name'],
            'first_name': request.form['first_name'],
            'middle_name': request.form['middle_name'],
            'address': request.form['address'],
            'phone': request.form['phone'],
            'birth_date': request.form['birth_date'],
            'location': request.form['location']
        }

        small_data.append(new_entry)
        return redirect(url_for('small_list'))

    return render_template('add_small.html')

@app.route('/elders_list')
def elders_list():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('elders_list.html', elders_data=elders_data)

@app.route('/add_elder', methods=['GET', 'POST'])
def add_elder():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        district = request.form.get('district')
        big_district = request.form.get('big_district')
        location = request.form.get('location')
        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        address = request.form.get('address')
        birth_date = request.form.get('birth_date')
        subscribers_count = request.form.get('subscribers_count')
        newspapers_count = request.form.get('newspapers_count')

        elders_data.append({
            'district': district,
            'big_district': big_district,
            'location': location,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'address': address,
            'birth_date': birth_date,
            'subscribers_count': subscribers_count,
            'newspapers_count': newspapers_count
        })

        return redirect(url_for('elders_list'))

    return render_template('add_elder.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ← отримує порт від Render
    app.run(host='0.0.0.0', port=port)
