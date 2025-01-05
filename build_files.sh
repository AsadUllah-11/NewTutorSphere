#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Collect static files without user input
python3.10 manage.py collectstatic --no-input
