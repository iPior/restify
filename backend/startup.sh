#! /usr/bin/bash

# create the virtual environment
# pip install Virtualenv
pyLocation=$(which python)
virtualenv -p $pyLocation venv
#activate script for venv
source venv/bin/activate

# install all required packages with pip
pip install -r requirements.txt

# run all migrations
python ./manage.py makemigrations
python ./manage.py migrate