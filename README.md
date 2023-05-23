# Goodeats

Imagine a world where you never have to search for a recipe again - instead, the perfect recipe comes to you, tailored to your individual tastes and dietary restrictions. That's the power of our integrated machine learning support, which analyses your preferences and recommends recipes that you're sure to love.

We've also built in features like collections, which allow you to organise and curate your favourite recipes, and user reviews, which help you discover new recipes and share your own experiences with the community. It's a platform that's both functional and fun.

Goodeats is a recipe sharing platform that uses cutting-edge machine learning technology to give users personalised recommendations, along with features like collections and user reviews to make sharing and discovering new recipes a breeze. The inspiration for our website name came from the wonderful website goodreads.

Our website uses an external ML API - [Recombee](https://www.recombee.com/) for giving user specific recipe recommendations based on their previous recipe interactions!

Hosted at [10.17.50.22](http://10.17.50.22) on the IITD Intranet.

Frontend development was done at https://github.com/rish106/goodeats-frontend

## Initial Plan
The API description [API Doc.yml](https://github.com/rish106/goodeats/blob/main/API_Doc.yml) was created using swagger and [ER diagram](https://github.com/rish106/goodeats/blob/main/ER_diagram.pdf) was made for the database design. A [Figma prototype](https://github.com/rish106/goodeats/blob/main/goodeats.fig) was made for the design of the web app. [Prototype demo](https://youtu.be/Rl7SulABLos)

## Languages/Frameworks used
- Next.js 13
- Tailwind CSS
- Typescript
- Flask
- MySQL

## Set up locally
You need to have [Node.js](https://nodejs.org/), [Python](https://www.python.org/) and [MySQL](https://www.mysql.com/) installed on your device.
- Create a new database using the following SQL command
```
CREATE DATABASE recipe_database;
```
- Put the dump in the new database using
```
mysql -u your_username -p recipe_database < backend/Dump.sql
```
- Enter the MySQL username and password in `backend/goodeats/__init__.py`
- Setup .env files in the frontend and backend directories.

`frontend/.env` should look like
```
BASE_API_URL='http://127.0.0.1:5000'
JWT_SECRET='mysecretkey'
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME='username'
```
`backend/.env` should look like
```
RECOMBEE_API_KEY='my_recombee_api_key'
```
- Install the backend requirements using
```
pip install -r backend/requirements.txt
```
- Start the flask server using
```
python3 backend/run.py
```
- Install the node modules using
```
cd frontend
npm install
```
- Start the frontend server using
```
npm run build
npm run start
```
- Enjoy Goodeats on http://localhost:3000
