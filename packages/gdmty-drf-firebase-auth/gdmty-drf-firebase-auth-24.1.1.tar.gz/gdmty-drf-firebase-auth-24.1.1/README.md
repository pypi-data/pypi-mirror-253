# gdmty-drf-firebase-auth

Firebase backend to receive a user idToken and authenticate via Django REST Framework 
'authentication.BaseAuthentication'. Optionally, a new local user can be created in the process.

## Requirements

* Python 3
* Django 4
* Django Rest Framework 3 
* Firebase Admin SDK

## Installation

```bash
$ pip install gdmty-drf-firebase-auth
```

## Configuration

Add the application to your project's `INSTALLED_APPS` in `settings.py`.

```python
INSTALLED_APPS = [
    # ...
    'gdmty_drf_firebase_auth',
    ...
]
```

### General settings

In your project's `settings.py`, add this to the `REST_FRAMEWORK` configuration. Note that if you want to retain access to the browsable API for locally created users, then you will probably want to keep `rest_framework.authentication.SessionAuthentication` too.

```python
REST_FRAMEWORK = {
  # ...
  'DEFAULT_AUTHENTICATION_CLASSES': [
    # ...
    'rest_framework.authentication.SessionAuthentication',  # Optional, better to remove for production
    'rest_framework.authentication.BasicAuthentication',  # Optional, better to remove for production
    'gdmty_drf_firebase_auth.authentication.FirebaseAuthentication',
  ]
}
```

The `gdmty_drf_firebase_auth` application comes with the following settings as default, which can be overridden in your project's `settings.py` file. For convenience, most of these can be conveniently set form environment variables also. Make sure to nest them within `DEFAULT_FIREBASE_AUTH_CONFIG` as below:

```python
DEFAULT_FIREBASE_AUTH_CONFIG = {
    # allow creation of new local user in db
    'FIREBASE_CREATE_LOCAL_USER': True,
    # attempt to split firebase user.display_name and set local user, first_name and last_name
    'FIREBASE_ATTEMPT_CREATE_WITH_DISPLAY_NAME': False,
    # Authorization header prefix, commonly JWT or Bearer (e.g. Bearer <token>)
    'FIREBASE_AUTH_HEADER_PREFIX': 'Bearer',
    # verify that JWT has not been revoked
    'FIREBASE_CHECK_JWT_REVOKED': True,
    # require that firebase user.email_verified is True
    'FIREBASE_AUTH_EMAIL_VERIFICATION': False,
    # function should accept firebase_admin.auth.UserRecord as argument and return str
    'FIREBASE_USERNAME_MAPPING_FUNC': map_firebase_uid_to_username
}
```

You can get away with leaving all the settings as default

### Firebase per-project settings

It is required to have GCP service accounts, the original project only supports one; the original code has been modified to allow more than one service account, To configure the service accounts, the following configuration must be added in the `settings.py` file of your project, where each element corresponds to a project and in turn, its respective service account.

`BASE_DIR` is the root of your project, where manage.py lives. We assume that you have a folder called `sa` in the root of your project, and that you have placed your service account keyfiles there. You can change this to wherever you like.

```python
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

...

FIREBASE_AUTH_SA_KEYFILES = {
    'project-1': os.path.join(BASE_DIR, 'sa', 'project-1-keyfile.json'),
    'project-2': os.path.join(BASE_DIR, 'sa', 'project-2-keyfile.json')
}

FIREBASE_AUTH_PROJECTS = {
    {'PROJECT_ID': 'project-1', 'SERVICE_ACCOUNT_KEY': FIREBASE_AUTH_SA_KEYFILES['project-1']},
    {'PROJECT_ID': 'project-2', 'SERVICE_ACCOUNT_KEY': FIREBASE_AUTH_SA_KEYFILES['project-2']},
}
```

Now that you have configured the application, run the migrations so that the Firebase data can be stored.

```bash
(venv) $ ./manage.py migrate gdmty_drf_firebase_auth
```

All you need to do now is have your client code handle the Firebase popup/redirect authentication flow, retrieve the idToken from the currentUser (Firebase explains this flow well in their docs: `https://firebase.google.com/docs/auth/admin/verify-id-tokens`), and then use the idToken for the user in an `Authorization` header in requests to your API.

```javascript
Bearer <token>
```

Now, all is ready!

## Contributing

* Please raise an issue/feature and name your branch 'feature-n' or 'issue-n', where 'n' is the issue number.
* If you test this code with a Python version not listed above and all is well, please fork and update the README to include the Python version you used :)

## Additional Notes

* This project is a fork of drf-firebase-auth, which seems no longer maintained. The original project only supports one service account, the original code has been modified to allow more than one service account.
* The initial proposal of this project had the option of use Firebase Auth with email and password, but this option was removed to keep the project clean and simple, and focused on the use of Firebase Auth with idToken for Django REST Framework.
* If you are looking for a project that supports Firebase Auth with email and password, you can use our side project: `gdmty-django-firebase-auth-email-password` at https://github.com/SIGAMty/gdmty-django-firebase-auth-email-password
* I almost always setup Django with a custom user class inheriting from AbstractUser, where I switch the USERNAME_FIELD to be 'email'. This backend is set up to assign a username still anyway, but if there are any issues, please raise them and/or make a pull request to help the community!
