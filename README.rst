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

Finaly, you will need to declare the app urls in your main urls.py file (don't forget the social_auth app urls there as well!). For exemple:

.. code-block::  python

    urlpatterns = patterns('',
        ...

        url(r'^facebook_canvas_auth', include('facebook_canvas_auth.urls')),
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
    
**************
Extra template
**************

In order to ease integration, ther eis a template you can include to your base layout which imports the facebook javascript SDK. It is by default set in en_US locale. 

In order to set it up, you need to do the following:

1/ Setup the FECEBOOK_APP_ID constant in your settings.py

.. code-block::  python

    FACEBOOK_APP_ID = '123456789'

2/ Add the following template processor so that the FACEBOOK_APP_ID is passed to all your tempaltes as the following variable facebook_app_id.

.. code-block::  python

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'facebook_canvas_auth.context_processors.get_facebook_app_id',
        ...
    )

3/ Include the template partial in the template where you need to use it.

.. code-block::  html

    {% include 'facebook_canvas_auth/facebook-sdk.html' %}
