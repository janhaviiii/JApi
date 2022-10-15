#!/bin/bash

echo start

echo please install python3, python3-pip, python3-django if not present

echo give name alt to Backend

read name

echo give alt name to BASE

read base

python3 -m venv env

echo check1

source env/bin/activate

echo check2

pip3 install django

echo check3

pip3 install djangorestframework

echo check4

django-admin startproject $name

echo check5

mv env/ $name/

echo check6

cd $name/

echo check7

python3 manage.py startapp $base

echo check8

python3 manage.py makemigrations

echo check9

python3 manage.py migrate

echo check10

python3 manage.py runserver

echo check11

echo DONE!
