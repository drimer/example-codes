Steps I'm following:

1: Install django with pip

2: Run `django-admin.py startproject mysite`

This creates the tree:
manage.py
mysite/
  __init__.py
  settings.py
  urls.py
  wsgi.py

4: Try running the development server: `python manage.py runserver`

5: Start the app blog: `python manage.py startapp blog`

6: Add the model `BlogPost`, and run `python manage.py syncdb` to make
django do the necessary changes in the database.

This command will prompt us if we want to add a superuser.

Note: I haven't configured the DB because b default, `settings.py`
already uses SQLite, which doesn't require any complex setup.

7: Play with the new model by using django's interactive shell:
`python manage.py shell`

8: Check that in the `urls.py` file, `admin.autodiscover()` is called.

9: Register the model BlogPost to the admin screens
(http://localhost:8000/admin) in its `admin.py` file.

10: Add BlogPostAdmin to specify what fields of the blog posts we want
to display in the admin screen.

11: Improve the looks of it (ie. ordering posts, use generic views,
ModelForm when possible, etc)
