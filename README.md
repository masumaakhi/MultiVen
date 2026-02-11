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