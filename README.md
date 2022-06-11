
<img src="https://user-images.githubusercontent.com/45036245/173190159-f3ff8fbc-0d56-4747-8b6a-0de34271e6ca.png" width="300"/>

# Django Boilerplate

A starter repo for a backend webservice with the following features:

- Basic Authentication for users
- Token authentication
- APIs for `/signup` and `/login`

## Setup

Run `git clone`

Run `pip install -r requirements.txt`

Run `./manage.py migrate`

Run `./manage.py runserver`

Once running the server you can use Postman (https://www.postman.com/) to explore the API URLs prefixed with `http://localhost:8000/api`

**Current API**

`/login/`

Verifies a username password match and returns a unique token specific to that user

`/signup/`

Creates a user with username and password and returns a unique token specific to that user

## Deployment

You can easily deploy this on either Heroku or Render with the following config

- The start command is `gunicorn backend.wsgi`
- The build command is `pip install -r requirements.txt`
- `PRODUCTION` environment variable should be `True`
- `EXTERNAL_HOSTNAME` should be whatever the URL is the provider gives you e.g. `something.onrender.com`

