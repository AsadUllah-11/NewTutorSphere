#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python3.10 manage.py collectstatic --noinput

echo "Build completed successfully."
