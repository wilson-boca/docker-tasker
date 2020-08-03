# Docker Tasker

Python scheduled tasks running on a docker-compose environment

### Installing

Installing requirements
```
$ mkvirtualenv tasker --python=python3
$ workon tasker
$ pip3 install -r requirements.txt
```

Running on terminal
```
Create your .env file based on .env.sample
Load your env variables
$ export $(cat .env | xargs)
$ python main.py
```

Running Celery
```
$ celery -A src.tasks.scheduled_tasks worker -B -Q celery -l DEBUG
```

Docker build
```
$ sudo docker build -t tasker .
```

Running docker-compose
```
Stop local Redis
$ /etc/init.d/redis-server stop
Run docker-compose
$ sudo docker-compose up -d
```
