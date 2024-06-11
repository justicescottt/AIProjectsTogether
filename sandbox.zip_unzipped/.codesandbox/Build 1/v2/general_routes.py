from flask import Blueprint, render_template

general_bp = Blueprint("general", __name__)


@general_bp.route("/")
def index():
    return render_template("index.html")


@general_bp.route("/about")
def about():
    return render_template("about.html")


@general_bp.route("/contact")
def contact():
    return render_template("contact.html")


@general_bp.route("/login")
def login():
    return render_template("login.html")


@general_bp.route("/terms")
def terms():
    return render_template("terms.html")


@general_bp.route("/legal")
def legal():
    return render_template("legal.html")
