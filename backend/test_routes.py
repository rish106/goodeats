import json
import pytest
from goodeats import app, db, bcrypt
from goodeats.models import User, Recipe,Keywords,Ingredients , Reviews , Collections
from flask import url_for
from flask_login import current_user
from goodeats.forms import UpdateProfileForm

def test_home(client):
    with app.app_context():
        response = client.get('/home')
        assert response.status_code == 200
        assert len(json.loads(response.data)) == 1
        
        user = User(username='testuser', name='Test User', email='test@example.com', password=bcrypt.generate_password_hash('testpassword').decode('utf-8'))
        recipe = Recipe(name='Test Recipe', author=user, description='A test recipe', instructions='Cook it and enjoy', ingredientAmt='1 cup of flour', cooktime='30 min', preptime='10 min', recipeServings=2)
        db.session.add(user)
        db.session.add(recipe)
        db.session.commit()
        
        response = client.get('/home')
        assert response.status_code == 200
        
def test_register(client):
    response = client.post('/register', json={
        'username': 'newuser',
        'name': 'New User',
        'email': 'newuser@example.com',
        'password': 'newpassword',
        'confirm_password': 'newpassword'
    })
    print(json.loads(response.data))
    assert response.status_code == 200
    assert json.loads(response.data)['message']== 'Your account has been created! You are now able to log in'
          
    response = client.post('/register', json={
        'username': 'newuser',
        'name': 'New User',
        'email': 'newuser@example.com',
        'password': 'newpassword',
        'confirm_password': 'newpassword'
    })
    assert response.status_code == 400
    assert json.loads(response.data)['username']== ['That username has already been taken. Please choose a different one.']

def test_profile_route(client):
        user = User(username='testuser', name='Test User', email='test@example.com', password='testpassword')
        db.session.add(user)
        db.session.commit()
        username = "testuser"
        response = client.get(url_for("profile", username=username))
        
        # Check that the response status code is 200
        assert response.status_code == 200
        
        # Check that the response data contains the expected keys and values
        expected_data = {'email': 'test@example.com', 
            'name': 'Test User', 
            'profile_picture': 'https://w0.peakpx.com/wallpaper/979/89/HD-wallpaper-purple-smile-design-eye-smily-profile-pic-face.jpg', 
            'user_id': 1, 
            'username': 'testuser'}
        print(json.loads(response.data))
        assert json.loads(response.data) == expected_data

def test_logout(client,login_user):
    response2 = client.post('/logout', follow_redirects=True)
    print(json.loads(response2.data))
    assert response2.status_code == 200 
    assert json.loads(response2.data)['message'] == 'You have been logged out'

def test_login_logout(client):
    user = User(username='testuser', name='Test User', email='test@example.com')
    db.session.add(user)
    db.session.commit()

    response = client.post('/login', json={
        'username': 'testuser', 
        'profile_picture': 'https://w0.peakpx.com/wallpaper/979/89/HD-wallpaper-purple-smile-design-eye-smily-profile-pic-face.jpg',
        'remember': 'false'
    })
    print(json.loads(response.data))
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'You have logged in successfully'

    # response3 = client.get('/check')
    # print(json.loads(response3.data))
    # assert response3.status_code == 200
    # # assert json.loads(response3.data)['message'] == 'You have logged in successfully'

    response2 = client.post('/logout', follow_redirects=True)
    print(json.loads(response2.data))
    assert response2.status_code == 200 
    assert json.loads(response2.data)['message'] == 'You have been logged out'

    response1 = client.post('/login', json={
        'username': 'testuser',
        'password': 'wrongpassword'
    })
    print(json.loads(response1.data))
    assert response1.status_code == 401
    assert json.loads(response1.data)['message'] == 'Username and password do not match'
