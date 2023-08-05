# snoozeWrites

# Steps To Run Locally and Make Changes
The following command are meant to run in a terminal or cmd
### First create a directory
    mkdir <dir_name>
### Change into to directory
    cd <dir_name>
### Clone this Repo to the present directory
    git clone https://github.com/Yaswanth14/snoozeWrites.git .
### Create a Virtual Environment
    python3 -m venv <env_name>
### Activate the Virtual Environment
    source <env_name>/bin/activate
### Install the required Dependencies using PIP
    pip install -r requirements.txt
### Make Migrations and Migrate To Create The Tables
    python manage.py makemigrations
    python manage.py migrate
### Create a Super User to Access the Admin Site
    python manage.py createsuperuser
### Run the Local Server on a specific Port
    python3 manage.py runserver
- By Default it runs on **127.0.0.1:8000**
### To Exit the Virtual Environment
    deactivate
