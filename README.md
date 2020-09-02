# Housing Market Analyzer
This is a project for COP4521. Housing Market Analyzer is a web based application that displays housing data taken from Zillow and shows a graph of it, along with a graph of perdicted housing data, based on a linear regression model. The data is generated and loaded to the database beforehand.

<br/>
Homescreen
<br/>
<img src="https://user-images.githubusercontent.com/19595312/91919103-e9327580-ec92-11ea-9ab0-ec87d2528002.PNG"/>

<br/>
Query
</br>
<img src="https://user-images.githubusercontent.com/19595312/91919105-e9327580-ec92-11ea-988b-31458bc012a4.PNG"/>

<br/>
Plotted Graphs
<br/>
<img src="https://user-images.githubusercontent.com/19595312/91919104-e9327580-ec92-11ea-8f43-53039cfcc857.PNG"/>

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

Run the script, and make sure that the newest database is created. If there are errors, delete the database and re-migrate

#### `python3 dataLoadScript.py HousingData/`

This will load in regular housing data

#### `python3 perdictedDataLoadScript.py DataAnalysis/`

This will load in data generated from the linear regression model.

### `python3 LinReg.py/`

This generates a csv containing predicted values based on the file <br/>`united-states (1).xls` <br/>
The lines <br/> `df = pd.read_excel("united-states (1).xls", sheet_name="Two Bed")` and <br/>
` df.to_csv("Predict Two Bed.csv")` </br>must be changed according to which sheet's dataset you want to load

## Enable linting in VScode

add the following to the settings.json file

```
"python.linting.pylintEnabled": true,
"python.linting.pylintArgs": [
    "--disable=C0111", // missing docstring
    "--load-plugins=pylint_django,pylint_celery",
 ],
```
