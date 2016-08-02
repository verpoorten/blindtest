# blindtest
Application to organize a musical quiz

## Contributing to the project

First, clone the project:

    $ mkdir python
    $ cd python
    $ mkdir projects
    $ cd projects
    $ git clone https://github.com/verpoorten/blindtest.git
    $ cd immobilier

### Creating a virtual environment

Check the version of Python you have installed in your machine using the command.

##### Ubuntu

    $ python3 --version
      Python 3.4.3

##### Windows

    $ python --version
      Python 3.4.3

The numbers that matter are 3 and 4. We use them to create a virtual environment on:

##### Ubuntu

Installing:

    # sudo apt-get install python-virtualenv

Creating:

    $ virtualenv --python=python3.4 venv
    $ chmod +x immovenv/bin/activate

Running:

    $ source venv/bin/activate

##### Windows

Creating:

    C:\Users\[Name]\python\projects\blindtest> C:\Python34\python -m venv venv

Running:

    C:\Users\[Name]\python\projects\blindtests> venv\Scripts\activate

### Installing Django

    (venv) $ pip install django

### Starting the app
    
    (venv) $ python manage.py migrate
    (venv) $ python manage.py makemigrations encoding
    (venv) $ python manage.py migrate encoding
    (venv) $ python manage.py runserver
    
After the restart, the application is available at http://localhost:8000.
    
### Developing

Everytime you change the model in any of the modules you have to generate a new migration file with the following command:

    (venv) $ python manage.py makemigrations encoding
    
The migration files will make sure the database is consistent with the code, so you won't have surprises while deploying your application. The command above will detect the changes you have made in your model, compare with the current database state and generate a script to migrate the database to the current state of your model. Sometimes this migration is not straitforward and you will have to answer some questions during the migration process. It should be done carefully to avoid inconsistencies.

In case you didn't put the application in production yet and you face a major problem on the migration, you can, as a last resource, start from scratch by deleting the database file and recreating it. For that, you just have to delete the file `db.sqlite3` located at the root of the project and perform the following commands:

    (venv) $ python manage.py migrate
    (venv) $ python manage.py createsuperuser

### Admin module

To access the admin module, you first have to create a user. Stop the server and run the following command:

    (venv) $ python manage.py createsuperuser
    
Follow the instructions and restart the server. To test your access, go to http://localhost:8000/admin and test your access.
