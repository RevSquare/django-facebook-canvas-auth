###########################
Django facebook canvas auth
###########################

Adds a layer to Django social auth to authenticate users in canvas or application tabs

These loaders work with the django-social-auth app. Please read the documentation for more information: http://django-social-auth.readthedocs.org/en/latest/

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

Add this line to your requirements.txt file:

.. code-block::  shell-session

    -e git+https://github.com/RevSquare/django-facebook-canvas-auth.git#egg=facebook-canvas-auth

And run:

.. code-block::  shell-session

    pip install -r requirements.txt

*****
Setup
*****

Before starting, make sure you have correctly setup django-social-auth: 

* http://django-social-auth.readthedocs.org/en/latest/installing.html
* http://django-social-auth.readthedocs.org/en/latest/configuration.html

This app basically adds a layer on top of *django social auth* to manage users automatic login via Facebook app canvas or tabs.

The first step is to add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'facebook-canvas-auth'
        ...
    )

The you will need to declare the loaders you want to add in your settings.py file

.. code-block::  python

    MIDDLEWARE_CLASSES = (
        ...
        'facebook-canvas-auth.middleware.FacebookCanvasAuth',
        ...
    )
    
******************
Settings constants
******************

At this stage nothing will be done. You can eventually setup a few constants.

*FACEBOOK_CANVAS_LOADING_MESSAGE*

This one allows you to customize the message displayed during the authentication canvas redirection. By default the message is "Facebook authentication" and it can be translated.

Usage exemple:

.. code-block::  python

    FACEBOOK_CANVAS_LOADING_MESSAGE = 'Facebook authentication'

*FACEBOOK_CANVAS_APP_TAB*

This settings constant is used to specify your facebook app tab in case you are using one.

Usage exemple:

.. code-block::  python

    FACEBOOK_CANVAS_APP_TAB = 'https://www.facebook.com/tabbApp/?sk=app_appnumber&ref=ts'
