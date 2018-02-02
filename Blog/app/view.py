from app import app
from flask import render_template

@app.route('/')
def index():
    comments=['nihao','123','asd','zxc']
    return render_template('tt.html',comments=comments)