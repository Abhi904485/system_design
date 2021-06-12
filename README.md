# Integrated Educative.io Grokking the Object Oriented Design Interview course With Django

## Python Version

```
3.8.3
```
## Install Necessary Modules 

```
pip install -r requirements.txt
```

## How to Run
```
python manage.py runserver
```
## For Postgres DB

```
 'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'db_host',
        'PORT': '3306',
    },
```
### Populate your DB from all_data.json fixture

```
python manage.py loaddata all_data.json --format json -e contenttypes
```

### Some Screenshots

![Home](cdn/static_root/images/home.png?raw=true "Home")

![Pagination](cdn/static_root/images/pagination.png?raw=true "Pagination")

![Problem Content](cdn/static_root/images/problem_content.png?raw=true "pPoblem Content")

![Use case](cdn/static_root/images/use_case.png?raw=true "Use case")

![Class](cdn/static_root/images/class.png?raw=true "Class")

![Java](cdn/static_root/images/java.png?raw=true "Java")

![Python](cdn/static_root/images/python.png?raw=true "Python")