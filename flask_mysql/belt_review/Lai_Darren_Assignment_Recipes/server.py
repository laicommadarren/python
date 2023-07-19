from recipes_app import app
from recipes_app.controllers import controllers_users, controllers_recipes
from recipes_app.models.models_user import User
from recipes_app.models.models_recipe import Recipe
if __name__=="__main__":
    app.run(debug=True)