from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random key

# Dummy user data for simplicity (In a real app, use a database)
users = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('about'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists!')
        else:
            users[username] = password
            session['username'] = username
            return redirect(url_for('about'))
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('about'))
        else:
            flash('Invalid username or password!')
    return render_template('login.html', title='Login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/about')
def about():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('about.html', title='About')

@app.route('/travel')
def travel():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('travel.html', title='Travel')

@app.route('/accommodation')
def accommodation():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('accommodation.html', title='Accommodation')

@app.route('/contact')
def contact():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html', title='Contact')

if __name__ == '__main__':
    app.run(debug=True)