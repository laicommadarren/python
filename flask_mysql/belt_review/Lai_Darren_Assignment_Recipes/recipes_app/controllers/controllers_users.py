from flask import render_template,redirect,request,session,flash
from recipes_app import app
from recipes_app.models.models_user import User
from recipes_app.models.models_recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    # validate the form here ...
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "email": request.form['email']
    }
    user_in_db = User.get_by_email(data)
    # check if email exists in database already
    if user_in_db:
        flash("An account with this email already exists.", 'category_reg')
        return redirect ('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User to save to database
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    session['user_first_name'] = data["first_name"]
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password combination", 'category_login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password combination", 'category_login')
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    session['user_first_name'] = user_in_db.first_name
    # never render on a post!!!
    return redirect('/dashboard')

# clears the session upon logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
