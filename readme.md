# news app
- this is based on the Django for beginners pdf

## added features
- superuser(admin) created
- User Authentication created
- Desiging using bootstrap (ongoing)

## errors
- nav bar error - displays over other text, when the browser is adjusted the nav bar shows as a small object with blank display

## fixed errors
- on creating users
``bash
    python manage.py startapp users
``
it didn't create a folder and cannot find the module users - fixed by reinstalling the django and by initiating command again
``bash
    python manage.py startapp users
``
