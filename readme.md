# news app
- this is based on the Django for beginners pdf

## added features
- superuser(admin) - created
- User Authentication - implemented
- Designing using bootstrap - created
- password change and reset - implemented
- creating the articles app - implemented
- permission and authorizations - implemented
- comments - implemented

## bugs
- 

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
``
    div style="padding-left: 65px;padding-right:65px"
``
fixed by adding padding to both sides

- reverse no match found for pk, missed this line on class comment
``
related_name='comments', 
``
now the card displays the footer which contains the comment.
- heroku deployment fixed by editing the Procfile, installing gunicorn, connecting github to heroku
``
    web: gunicorn newspaper_project.wsgi --log-file -
``
- deleting - on confirm error

## Deployment

To deploy this project copy this code and paste it on your broswer

```bash
  https://newspaperwebapp.herokuapp.com/
```

## QA Comments
Current issues found:  
  
USER  
-Age field on Sign Up page allows ages 0 and beyond 100.  
-Usage of same email by multiple users is currently allowed.  
-Can't delete his/her own published news, results in NoReverseMatch error.  
  
ADMIN  
-Can't delete his/her own published news nor those of the users, results in NoReverseMatch error.  
  
WEB APP  
-Created users disappear after some time.  (dev- caching in not yet implemented)
-Can only access user accounts on machines where they are created. (dev- caching in not yet implemented)

## Contributing
-[@christophernabo](https://github.com/christophernabo)  
-[@MaFloresTuscano](https://github.com/MaFloresTuscano)


