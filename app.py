from flask import Flask, render_template
# import  data_flow as df
from data_flow import data_handler
app = Flask(__name__)



# Route for the Home page
@app.route('/')
def home():
    handler = data_handler.data_handler()
    df = handler.read_data()
    print('in home')
    print(df)
    return render_template('home.html',emails=df)

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
