from flask import Flask, render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from models import Product, User
from forms import AddInformationForm, RegisterForm, EditInformationForm, LoginForm
from ext import application, database


@application.route("/")
def home():
    sources = Product.query.all()
    return render_template("index.html", sources=sources)


@application.route("/source/<int:source_id>")
def view_source(source_id):
    chosen_source = Product.query.get(source_id)
    return render_template("detailed.html", source=chosen_source)


@application.route("/add_information", methods=["POST", "GET"])
@login_required
def add_information():
    if current_user.role != "admin":
        return redirect("/")
    form = AddInformationForm()
    if form.validate_on_submit():
        print(form.img.data)

        new_information = Product(name=form.name.data, subtext=form.subtext.data, text=form.text.data,
                                  img=form.img.data.filename)
        database.session.add(new_information)
        database.session.commit()

        form.img.data.save(f"{application.root_path}\\static\\{form.img.data.filename}")

        return redirect("/")
    return render_template("add_information.html", form=form)


@application.route("/edit/<int:source_id>", methods=["POST", "GET"])
@login_required
def edit_product(source_id):
    chosen_source = Product.query.get(source_id)

    if current_user.role != "admin":
        return redirect("/")

    form = EditInformationForm(editname=chosen_source.name, editsubtext=chosen_source.subtext,
                               edittext=chosen_source.text, source=chosen_source)
    if form.validate_on_submit():
        chosen_source.name = form.editname.data
        chosen_source.subtext = form.editsubtext.data
        chosen_source.text = form.edittext.data

        if form.editimg.data != None:
            chosen_source.img = form.editimg.data.filename
            form.editimg.data.save(f"{application.root_path}\\static\\{form.editimg.data.filename}")
        database.session.commit()
        return redirect("/")

    return render_template("edit_information.html", form=form)


@application.route("/delete/<int:source_id>")
@login_required
def delete_product(source_id):
    chosen_source = Product.query.get(source_id)
    if current_user.role != "admin":
        return redirect("/")
    database.session.delete(chosen_source)
    database.session.commit()
    return redirect("/")


@application.route("/Sponsors")
def Sponsors():
    return render_template("sponsors.html")


@application.route("/register", methods=["POST", "GET"])
def Registration():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            error_message = "სახელი დაკავებულია, გთხოვთ აირჩიოთ სხვა"
            return render_template("register.html", form=form, error_message=error_message)
        else:
            new_user = User(username=form.username.data, password=form.password.data, gender=form.gender.data,
                            birthday=form.birthday.data, country=form.country.data, role="visitor")
            new_user.create()
        return redirect("/")

    return render_template("register.html", form=form)


@application.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    error_message = None
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        else:
            error_message = "შეყვანილი პაროლი არასწორია"

    return render_template("login.html", form=form, error_message=error_message)


@application.route("/logout")
def logout():
    logout_user()
    return redirect("/")
