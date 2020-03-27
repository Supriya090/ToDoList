from flask import Flask, render_template

# creates a Flask application, named app
Flaskapp = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template("Homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
