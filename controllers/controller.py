from flask import render_template
from app import app
from models.classes.books_ordered import order_list

@app.route('/')
def index():
    return render_template('index.html', title="Bookshop")
