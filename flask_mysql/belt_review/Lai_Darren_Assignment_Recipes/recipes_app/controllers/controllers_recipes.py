from flask import render_template,redirect,request,session,flash
from recipes_app import app
from recipes_app.models.models_user import User
from recipes_app.models.models_recipe import Recipe

# landing page showing all recipes
@app.route('/dashboard')
def dashboard():
    if not session:
        flash("You can only access the dashboard after registration or login.", 'category_db')
        return redirect('/')
    return render_template("dashboard.html", recipes=Recipe.get_all_recipes(), name = session['user_first_name'], id = session["user_id"])

@app.route('/recipes/new')
def new_recipe():
    if not session:
        flash("You can only access this page after registration or login.", 'category_db')
        return redirect('/')
    return render_template('newrecipe.html', id=session["user_id"])

@app.route('/recipes/create', methods=["POST"])
def create_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("show_recipe.html", recipe=Recipe.get_one_recipe(data))

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if not session:
        flash("You can only access this page after registration or login.", 'category_db')
        return redirect('/')
    data = {
        "id": id
    }
    return render_template("edit_recipe.html", recipe=Recipe.get_one_recipe(data))

@app.route('/recipes/update', methods=["POST"])
def update():
    id= request.form['id']
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{id}")
    Recipe.update(request.form)
    return redirect('/dashboard')

# DELETE recipe
@app.route('/recipes/destroy/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')
