from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("viewbook.html")

@views.route('GSB', methods=['GET'])
def students_book():
    return render_template("students_book.html")