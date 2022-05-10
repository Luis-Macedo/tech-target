
# Tech Target project

Tech Target is a CMI plataform that includes data analisys and community integration,
providing technical support for startups and small business.
 

## Installation - dev environment for python (venv)

Install techTarget backend with python 3.9+/ pip and venv.

```bash
  py -m pip install venv
  or python -m pip install venv
```
## Installation - Setting the environment inside the repository

Inside the techTarget repository (where src directory is also located), run the
following commands (Windows):

```bash
  py -m venv venv
  /venv/Scripts/activate.ps1
```
At this point you'll be able to have a python environment for proper working alongside Django

## Installation - Installing Django

Now, we install Django

```bash
  pip install Django
```

Once installed, you can change to src directory

## Installation - Inside de src directory

### Before going into the steps ahead, be sure to setup your database connection 
### Your database connection will be inside src/techTarget/settings.py

Once you have setup your database, you'll run the following commands for migrations:

```bash
  python manage.py makemigrations
  python manage.py migrate
```
### After migrating the models, the next step is filling the location tables with the script called 'locations.py', inside 'cities_and_states' (Be sure to also setup your database there)

## Testing

Now, you're ready to go with testing. All you need to do is running the following command:

```bash
  python manage.py runserver
```




## Features

- Database used: PostgreSql
- Database name: techtarget


