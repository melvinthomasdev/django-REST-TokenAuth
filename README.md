# django-REST-TokenAuth
A django app that can be added to your projects to implement TokenAuthentication.

## Features
- Custom User model with email as the username field.
- Extendable `UserProfile` model to add additional fields to the user.
- TokenAuthentication for API endpoints.

## Before you start 
- please ensure that you do not have any migrations applied to the database. Otherwise, it may cause issues.
- It is advised you add this app right after creating the project, before running any migrations. 

## How to  use
1. Clone this repository and copy the accounts directory to your project root directory.
2. Install requirements using `pip install -r accounts/requirements.txt`
3. Add the following to your INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'import_export',

    'accounts',
    ...
]
```
3. Set "AUTH_USER_MODEL" in settings.py to "accounts.User"
```python
AUTH_USER_MODEL = 'accounts.User'
```
4. Add the following at the end of settings file
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```
5. In urls.py add the following
```python
url = [
    ...
    path('account/', include('accounts.urls')),
    ...
]
```
6. Run migrations using `python manage.py migrate`
7. Now you can register a superuser using `python manage.py createsuperuser` and start using the API with TokenAuthentication.
8. Refer to the [API Documentation Available here](https://documenter.getpostman.com/view/10665006/VVBXxRK7) for more details.

## Contributing 
- Fork the repository
- Create a new branch
- Make your changes
- Create a pull request


### Please Star the repo and share it with your friends if you find it useful. Follow me for more such projects.