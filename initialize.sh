#!/bin/bash

echo start

echo please install python3, python3-pip, python3-django if not present

echo give name alt to Backend

read name

echo give alt name to BASE

read base

python3 -m venv env

echo Created virtual enviornment

source env/bin/activate

echo Activated virtual enviornment

pip3 install django

echo Installed django successfully

pip3 install djangorestframework

echo Installed djangorestframework successfully

django-admin startproject $name

echo Started project $name

mv env/ $name/

echo Moved virtual enviornment to $name folder

cd $name/

echo Changed directory to $name folder

python3 manage.py startapp $base

echo Started new App $base

python3 manage.py makemigrations

echo Converted python models to SQL classes

python3 manage.py migrate

echo Created database Successfully

python3 manage.py runserver

echo Server Running

echo DONE!
