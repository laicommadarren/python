from recipes_app.config.mysqlconnection import connectToMySQL
from flask import flash, session, request, flash
from recipes_app.models import models_recipe

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('recipes_schema').query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 letters.", 'category_reg')
            print('First name invalid')
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 letters.", 'category_reg')
            print('Last name invalid')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Email format is not valid.", 'category_reg')
            print('Email format invalid')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", 'category_reg')
            print('Password requirements not met')
            is_valid = False
        if not user['confirm_password'] == user['password']:
            flash("Passwords do not match.", 'category_reg')
            print('Passwords do not match')
            is_valid = False
        return is_valid
    
    