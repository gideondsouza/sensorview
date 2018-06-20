from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Main"

@main.route('books/')
def display_books():
    books = {
        "A": "Gideon D",
        }

    # passing data to the template
    return render_template("home.html", books=books)

