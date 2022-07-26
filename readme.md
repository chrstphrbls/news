# news app
- this is based on the Django for beginners pdf

## added features
- superuser(admin) - created
- User Authentication - created
- Designing using bootstrap - created
- password change and reset - created
- creating the articles app - created
- permission and authorizations - created
- comments - ongoing

## bugs
- deploying on heroku, command syntax error.

## fixed bugs
- nav bar error - displays over other text, when the browser is adjusted the nav bar shows as a small object with blank display, fixed by adding this to the code
```
    <!-- <div style="padding:65px"> --> 
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark mb-4">
```
- on creating users
``
    python manage.py startapp users
``
it didn't create a folder and cannot find the module users - fixed by reinstalling the django and by initiating command again
``
    python manage.py startapp users
``
also by commenting the line which installs the app in the setting.py - project directory
- the body is very close to the sides
```
    <div style="padding-left: 65px;padding-right:65px">
```
- fixed by adding padding to both sides

- reverse no match found for pk, missed this line on class comment
``
related_name='comments', 
``
now the card displays the footer which contains the comment.