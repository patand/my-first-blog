@echo off

START http://127.0.0.1:8000/

cd /

C:

cd planning_03_03_16



cmd /k "env\scripts\activate & cd projet2 & python manage.py runserver"


cmd /k
