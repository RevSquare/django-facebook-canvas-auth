from django.conf import settings


def get_facebook_app_id(request):
    """
    Adds by default the facebook app id in the templates to communicate with \
    facebook. If FACEBOOK_APP_ID is not set in the settings.py, let the \
    application raises an ImportError.
    :returns:  A formated django response
    :rtype: obj
    """
    return {'facebook_app_id': settings.FACEBOOK_APP_ID}
