from flask import render_template, request
from werkzeug.utils import redirect

import dao
from saleapp import app, login, admin
import math
from flask_login import login_user, current_user, logout_user

@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    prods = dao.load_products(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_products()/app.config["PAGE_SIZE"])
    return render_template("index.html", prods=prods, pages=pages)

@app.route("/products/<int:id>")
def details(id):

    return render_template("products-details.html", prod=dao.get_product_by_id(id))

@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categories()
    }

@app.route("/login", methods=['get', 'post'])
def login_my_user():
    err_msg = None
    if current_user.is_authenticated:
        return redirect("/")
    if request.method.__eq__('POST'):
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_user(username, password)

        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Username or password is not right!"
    return render_template("login.html", err_msg=err_msg)

@app.route("/logout")
def logout_my_user():
    logout_user()
    return redirect("\login")


@login.user_loader
def get_user(id):
    return dao.get_user_by_id(id)

if __name__== "__main__":
    with app.app_context():
        app.run(debug=True)
