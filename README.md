# RECIPE-APP-API
Recipe API project

## Dev Methodology
- Test Driven Development (TDD)
- Docker: Ensures consistency between development and production environments by capturing all dependencies as code.
- GitHub Actions: Automation tool for running unit tests, code linting, and deployment.

## Important Commands
```bash
docker-compose -f docker-compose-deploy.yml up --no-deps -d app
sh -c "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"



## Deployment and Prerequisites
### Steps
1. Configure the project for deployment.
2. Create a virtual server on AWS.
3. Deploy the app.

# Prerequisites
- Install Docker, Docker Compose, and Git on the AWS EC2 instance.


