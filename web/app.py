from flask import Flask, redirect, url_for, render_template


app = Flask(__name__,template_folder='template')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)