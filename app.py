from flask import Flask, render_template, request, redirect, url_for, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse

# Library Pendukung:
# - pip install flask-sqlalchemy
# - pip install werkzeug
# - pip install SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@localhost/quizkita"
app.config["SECRET_KEY"] = "Muhamad Ibnu"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    marks = db.Column(db.Integer, index=True)

    def __repr__(self):
        return "<User {}>".format(self.username) # Mengembalikan string yang merepresentasikan kelas Username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Questions(db.Model):
    q_id = db.Column(db.Integer, primary_key=True)
    ques = db.Column(db.String(350), unique=True)
    a = db.Column(db.String(100))
    b = db.Column(db.String(100))
    c = db.Column(db.String(100))
    d = db.Column(db.String(100))
    ans = db.Column(db.String(100))

    def __repr__(self):
        return "<Question: {}>".format(self.ques) # Mengembalikan string yang merepresentasikan kelas Questions

with app.app_context():
    db.create_all() # Perintah untuk membuat database yang didefinisikan oleh model FlaskSQLAlchemy


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")
    # DataRequired = validator yang harus diisi jika kosong maka formulir tidak dapat diterima/ memunculkan error.


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=(DataRequired(), Email()))
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Confirm Password", validators=(DataRequired(), EqualTo("password"))
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username Sudah Digunakan")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email Sudah Digunakan")


class QuestionForm(FlaskForm):
    options = RadioField("Options: ", validators=[DataRequired()], default=1)
    submit = SubmitField("Next")


@app.before_request
def before_request():
    g.user = None 

    if "user_id" in session:
        user = User.query.filter_by(id=session["user_id"]).first()
        g.user = user


@app.route("/")
def home():
    return render_template("index.html", title="Halaman Utama")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
        session["user_id"] = user.id
        session["marks"] = 0
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("home")
        return redirect(next_page)
    if g.user:
        return redirect(url_for("home"))
    return render_template("login.html", form=form, title="Login")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        session["marks"] = 0
        return redirect(url_for("home"))
    if g.user:
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/question/<int:id>", methods=["GET", "POST"])
def question(id):
    form = QuestionForm()
    q = Questions.query.filter_by(q_id=id).first()
    if not q:
        return redirect(url_for("score"))
    if not g.user:
        return redirect(url_for("login"))
    if request.method == "POST":
        option = request.form["options"]
        # print("Selected Option:", option)
        # print("Correct Answer:", q.ans)
        print(session['marks'])
        if option == q.ans:
            session["marks"] += 10
        next_question_id = id + 1 
        if next_question_id > 10:
            return redirect(url_for("score"))
        return redirect(url_for("question", id=(id+1)))
    form.options.choices = [(q.a, q.a), (q.b, q.b), (q.c, q.c), (q.d, q.d)]
    return render_template(
        "question.html", form=form, q=q, title="Question {}".format(id)
    )

@app.route("/score")
def score():
    if not g.user:
        return redirect(url_for("login"))
    g.user.marks = session["marks"]
    db.session.commit()
    return render_template("score.html", title="Nilai Akhir")


@app.route("/logout")
def logout():
    if not g.user:
        return redirect(url_for("login"))
    session.pop("user_id", None)
    session.pop("marks", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)