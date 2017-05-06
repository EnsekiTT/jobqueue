# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Set your own key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    flash(u"Add job queue!!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
