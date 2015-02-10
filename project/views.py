from flask import render_template, url_for
from app import app, pages

@app.route('/')
def home():
    return render_template('index.html')
    # return 'Hello World!'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
