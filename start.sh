#!/bin/bash

source env/bin/activate
pip install -r requirements.txt
./manage.py makemigrations
./manage.py migrate
