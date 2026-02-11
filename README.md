Setup for MySQL Database:

1.  cmd: pip install mysqlclient
2. mysql shell: CREATE DATABASE my_django_db;
3. project er setting.py: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_django_db',       # ডাটাবেসের নাম
        'USER': 'root',                # আপনার MySQL ইউজারনেম
        'PASSWORD': 'your_password',   # আপনার MySQL পাসওয়ার্ড
        'HOST': 'localhost',           # অথবা '127.0.0.1'
        'PORT': '3306',                # MySQL-এর ডিফল্ট পোর্ট
    }
}

4. cmd: python manage.py makemigrations
5. cmd: python manage.py migrate
6. cmd: python manage.py runserver
Jodi mysqlclient error ase tahole cmd: python -m pip install --upgrade mysqlclient or pip istall pymysql
tarpore project er __init__.py:
 import pymysql
pymysql.version_info = (2, 2, 4, "final", 0) # Fake the version for Django
pymysql.install_as_MySQLdb()

** pip install cryptography
**python -m pip show mysqlclient
**python -m pip install --upgrade pip
**python -m pip install mysqlclient==2.2.4

For Venv active:
python -m venv venv
venv\Scripts\activate

For venv deactivate


Setup for PostgreSQL:
1. pip install psycopg2-binary
2. settings.py:
        DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',                # আপনার তৈরি করা ডাটাবেসের নাম
        'USER': 'postgres',            # ডিফল্ট ইউজার সাধারণত এটাই থাকে
        'PASSWORD': 'your_password',   # PostgreSQL ইন্সটলের সময় যে পাসওয়ার্ড দিয়েছিলেন
        'HOST': '127.0.0.1',           # লোকাল পিসির জন্য 127.0.0.1 বা localhost
        'PORT': '5432',                # PostgreSQL এর ডিফল্ট পোর্ট
    }
}

3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py runserver