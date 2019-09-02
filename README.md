# simple_twitter_app

# This app can be deployed using Docker Compose 3.


# Linux instructions and terminal commands:

# In order to build the Docker image and start the test server, enter the directory with cloned repository and run this command in terminal:
# Start by building the image:
docker-compose build

# Apply database migrations:
docker-compose run --rm app sh -c "python manage.py migrate"

# Start development server:
docker-compose up

# If you wish to access Django admin site, create a superuser (it can be done from another terminal at the same directory while the test server is running)
docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Test suite and code style guide can be ran with the following command:
docker-compose run --rm app sh -c "python manage.py test && flake8"

# Web browser instructions:
- Check the Django start page at 127.0.0.1:8000
- Check the Django admin page at 127.0.0.1:8000/admin/ and log in using the
  superuser credentials if you have created one (instructions above)
- In case of any problems please contact the owner of this repository

# User-management API
- Register new user:
127.0.0.1:8000/api/user/create
- Generate access token:
127.0.0.1:8000/api/user/token
- Edit user data (pass like "Token 6716821995f528c059207b0e266049efbcb7d053" to HTTP request "Authorization" header - use your hash number; for testing in a browser use Modify Header extension):
127.0.0.1:8000/api/user/me

# Tweet-management API
- Create new tweet:
127.0.0.1:8000/api/tweets/create/
- Retrieve tweets for given tag (tag2 is the tag string being looked up):
127.0.0.1:8000/api/tweets/retrieve/?tag=tag2
- Display number of tweets per year for the given timeframe:
127.0.0.1:8000/api/tweets/count/?from=2015&till=2020
- Display number of tweets per year for specific tag per timeframe:
127.0.0.1:8000/api/tweets/count/?from=2015&till=2020&tag=tag2
