#!/bin/bash
set -e

echo "Starting SSH and Celery..."
service ssh start

celery -A src.tasks.scheduled_tasks worker -B -Q celery -l INFO