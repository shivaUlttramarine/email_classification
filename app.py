from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the About page
@app.route('/user')
def user():
    return render_template('user.html')

# Route for the Contact page
@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
