# news app
- this is based on the Django for beginners pdf

## added features
- superuser(admin) - created
- User Authentication - created
- Designing using bootstrap - created
- password change and reset - created
- creating the articles app - created
- permission and authorizations - ongoing

## errors
- deploying on heroku, command syntax error.

## fixed errors
- nav bar error - displays over other text, when the browser is adjusted the nav bar shows as a small object with blank display, fixed by adding this to the code
``html
    <!-- <div style="padding:65px"> --> 'replaced'
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark mb-4">
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
- the body is very close to the sides
`` html
    <div style="padding-left: 65px;padding-right:65px">
``
added padding to both sides

