## Make Sure the follwing is installed
pip3 `sudo apt install python3-pip`
venv `sudo apt-get install -y python3-venv`

## Setup
Create a virtual environment with:

#### `python3 -m venv env`
then activate it with: 
#### `source env/bin/activate`

Install the dependencies with:
#### `pip3 install -r requirements.txt`
There may be a warning after the installation, but if it the django runserver command works its fine.

## Start Django 
To start the Django server:
#### `python3 manage.py runserver`

## Reset Database
Delete the `db.sqlite3` and all files inside of `data/migrations` then run 
#### `python3 manage.py makemigrations data` and `python manage.py migrate`
Create a super user afterwards to access the admin pannel

## Load test data
Run the command 
#### `python3 manage.py loaddata testdata.json`

## Enable linting in VScode
add the following to the settings.json file 
```
"python.linting.pylintEnabled": true,
"python.linting.pylintArgs": [
    "--disable=C0111", // missing docstring
    "--load-plugins=pylint_django,pylint_celery",
 ],
 ```