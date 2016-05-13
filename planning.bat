@echo off

START http://127.0.0.1:8000/

cd /

C:

cd planning5



cmd /k "env\scripts\activate & cd projet2 & python manage.py runserver"

































