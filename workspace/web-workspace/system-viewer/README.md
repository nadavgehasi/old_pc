# system-viewer

### Backend

Deployed on AWS
- http://system-viewer.us-east-1.elasticbeanstalk.com/

Technologies used:
- Python 3.8
- Django 3.0
- Django Rest framework
- Docker
- Docker-compose
- Poetry
- Pyenv
- AWS Elastic Beanstalk

#### Developer notes

##### How to run?
1. Run on local computer
   ```shell script
   cd backend
   poetry install
   poetry run pip install -r requirements.txt
   ./run.sh
   rm -r database
   ```

2. Run with docker
   ```shell script
   docker build -t system-viewer-backend backend
   docker run -v backend-storage:/myapp/database/ -p 8000:8000 --name backend -d system-viewer-backend
   docker stop backend
   docker rm backend
   ```

3. Run with docker compose
   ```shell script
   docker-compose build
   docker-compose up -d
   docker-compose down -v
   ```
