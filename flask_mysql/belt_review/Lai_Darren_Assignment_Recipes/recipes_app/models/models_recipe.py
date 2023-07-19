from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request, flash
from recipes_app.models import models_user

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.recipe = data['recipe']
        self.datecookedmade = data['datecookedmade']
        self.underthirtymin = data['underthirtymin']
        self.user_id = session['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, recipe, user_id, datecookedmade, underthirtymin, created_at, updated_at) VALUES (%(name)s, %(description)s, %(recipe)s, %(user_id)s, %(datecookedmade)s, %(underthirtymin)s, NOW(), NOW())"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * from recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;"
        result = connectToMySQL('recipes_schema').query_db(query, data)
        # recipeinfo = 
        recipe = cls(result[0])
        for row in result:
            user_data = {
                "id" : row["users.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "email" : row["email"],
                "password" : row["password"],
                "created_at" : row["users.created_at"],
                "updated_at" : row["users.updated_at"]
            }   
            recipe.user = (models_user.User(user_data))
        return recipe

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, recipe=%(recipe)s, datecookedmade=%(datecookedmade)s, underthirtymin=%(underthirtymin)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL('recipes_schema').query_db(query, data)
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * from recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipeslist = []
        for row_from_db in results:
            recipe = cls(row_from_db)
            user_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at" : row_from_db["users.created_at"],
                "updated_at" : row_from_db["users.updated_at"]
            }
            recipe.user = (models_user.User(user_data))
            recipeslist.append(recipe)
        return recipeslist
    
    @classmethod
    def get_user_firstname_from_recipe(cls):
        query = "SELECT first_name FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query)
        return results
        
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if not recipe['name']:
            flash("Recipe name cannot be empty.")
        elif len(recipe['name']) < 3:
            flash("Recipe name must be at least 3 characters.")
            is_valid = False
        if not recipe['description']:
            flash("Recipe description cannot be empty.")
        elif len(recipe['description']) < 3:
            flash("Recipe description must be at least 3 characters.")
            is_valid = False
        if not recipe['recipe']:
            flash("Recipe instructions cannot be empty.")
            is_valid = False
        elif len(recipe['recipe']) < 3:
            flash("Recipe instructions must be at least 3 characters.")
            is_valid = False
        if not recipe['datecookedmade']:
            flash("Date Cooked/Made cannot be empty.")
            is_valid = False
        return is_valid
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL('recipes_schema').query_db(query, data)