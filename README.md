# to add database
* add entry on model.py

```
python3 manage.py makemigrations
python3 manage.py migrate
```


```asciidoc
python3 manage.py sqlmigrate HomEApp 0001

```


<!--{%include "dashboard_headder.html" %}-->
# for static files
```
python manage.py collectstatic
```