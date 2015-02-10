from flask import render_template, url_for
from app import app

@app.route('/')
def about():
    return render_template('about.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')
