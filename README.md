# simple_twitter_app

# This app can be deployed using Docker Compose 3.


# Linux instructions:

# In order to build the Docker image and start the test server, enter
# the directory with cloned repository and run this command in terminal:
docker-compose up

# If you wish to access Django admin site, create a superuser (it can be done
# from another terminal at the same directory while the test server is running)
docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Test suite and code style guide can be ran with the following command:
docker-compose run --rm app sh -c "python manage.py test && flake8"


# Web browser instructions:

# - Check the Django start page at 127.0.0.1:8000
# - Check the Django admin page at 127.0.0.1:8000/admin and log in using the
#   superuser credentials if you have created one (instructions above)
# - In case of any problems please contact the owner of this repository
