# news app
- this is based on the Django for beginners pdf

## added features
- superuser(admin) - created
- User Authentication - created
- Designing using bootstrap - created
- password change and reset - created
- creating the articles app - ongoing

## errors


## fixed errors
- nav bar error - displays over other text, when the browser is adjusted the nav bar shows as a small object with blank display, fixed by adding a padding 
``css
    <div style="padding:65px">
``
- on creating users
``bash
    python manage.py startapp users
``
it didn't create a folder and cannot find the module users - fixed by reinstalling the django and by initiating command again
``bash
    python manage.py startapp users
``
, also by commenting the line which installs the app in the setting.py - project directory


