import os
print(os.getcwd())
os.chdir('PP1')
print(os.getcwd())
os.system('python manage.py runserver')