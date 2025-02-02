import os
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
from dotenv import load_dotenv

load_dotenv()
RECOMBEE_API_KEY = os.getenv('RECOMBEE_API_KEY')
client = RecombeeClient('goodeats-dev', RECOMBEE_API_KEY)

def recipe_user(user_id):
    recommeded_recipes = (client.send(RecommendItemsToUser(str(user_id), 20)))['recomms']
    recipe_list = []
    for recipe in recommeded_recipes:
        recipe_list.append(int(recipe['id']))
    return recipe_list

def user_user(user_id):
    recommeded_users = (client.send(RecommendUsersToUser(str(user_id), 20)))['recomms']
    user_list = []
    for recipe in recommeded_users:
        user_list.append(int(recipe['id']))
    return user_list

def add_user(user):
    response = client.send(SetUserValues(
        str(user.id),
        {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'image_file': user.image_file
        }, cascade_create=True
    ))
    return response

def add_recipe(recipe, author):
    response = client.send(SetItemValues(
        str(recipe.id),
        {
            'recipeID': recipe.id,
            'name': recipe.name, 
            'CookTime': recipe.cooktime,
            'PrepTime' : recipe.preptime,
            'AuthorName': author.username,
            'user_ID': author.id
        }, cascade_create=True
    ))
    return response

def add_view(user_id, recipe_id):
    response = client.send(AddPurchase(str(user_id), str(recipe_id)))
    return response

def add_rating(user_id, recipe_id, rating):
    rate = (rating-3)/2
    response = client.send(AddRating(str(user_id), str(recipe_id), rate))
    return response

def add_bookmark(user_id, recipe_id):
    response = client.send(AddBookmark(str(user_id), str(recipe_id), cascade_create=True))
    return response
