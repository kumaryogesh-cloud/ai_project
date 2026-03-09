from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

users_db=[]

# 1. Yeh route HTML webpage dikhayega
@app.route('/')
def home():
    # Hum yahan se data bhej rahe hain jo template mein dikhega
    user_info = {
        "name": "Python Developer",
        "role": "Backend Specialist"
    }
    return render_template('index.html', user=user_info)
# --- Registration ka code yahan se shuru ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users_db.append({"username": username, "password": password})
        return redirect(url_for('login'))
    return render_template('register.html')

# --- Login ka code yahan se shuru ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_msg = ""
    if request.method == 'POST':
        u_name = request.form.get('username')
        p_word = request.form.get('password')
        for user in users_db:
            if user['username'] == u_name and user['password'] == p_word:
                return f"<h1>Welcome {u_name}! Login Successful.</h1>"
        error_msg = "Galat details!"
    return render_template('login.html', error=error_msg)

# 2. Yeh ek simple GET API endpoint hai jo JSON data return karega
@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "Success",
        "message": "API sahi kaam kar rahi hai!"
    })

if __name__ == '__main__':
    app.run(debug=True)