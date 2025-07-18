from flask import Flask, render_template, request, redirect, session, url_for
from users import users
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 🔐 Заміни на свій

big_data = []

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


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # ← отримує порт від Render
    app.run(host='0.0.0.0', port=port)
