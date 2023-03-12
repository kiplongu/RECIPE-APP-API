# RECIPE-APP-API
Recipe API project

# Dev Methodology
--Test Driven Development TDD

--Docker- for consistency dev and prod environment as it captures all dependencies as code
--Github actions- Automation tool for unit tests, code linting and deployment



# Important commands
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
sh -c python manage.py wait_for_db
             python manage.py migrate
             python manage.py runserver 0.0.0.0:8000


# Deployment and prerequisites
--steps.
Configured project for deployment
Created virtual server on AWS
Deployed the app

-Install Docker, Docker-compose and Git on AWS ec2 instance

