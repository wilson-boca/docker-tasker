#!/bin/bash
set -e
echo "Starting Flask API ..."
gunicorn --workers=2 --bind 0.0.0.0:8000 app.main:app