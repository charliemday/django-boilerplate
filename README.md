# boilerplate-backend
Starter for using Django Rest Framework with some Authentication using Django Tokens

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
