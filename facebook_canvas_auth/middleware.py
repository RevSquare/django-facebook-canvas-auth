# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from social_auth.middleware import SocialAuthExceptionMiddleware
from social_auth.exceptions import AuthCanceled


FACEBOOK_CANVAS_LOADING_MESSAGE = "Facebook authentication"


class FacebookCanvasAuth(SocialAuthExceptionMiddleware):
    """
    Middleware managing the facebook authentication via canvas.
    """
    def process_request(self, request):
        """
        Handles the redirections to login specific steps \
        according to the request type.
        :param request: Django request object.
        :type item: obj
        :returns:  A formated django response
        :rtype: obj
        """
        if 'facebook' in request.META['HTTP_USER_AGENT']:
            return

        redirection = reverse('add_check_user_loggedin')

        if not request.user.is_authenticated() \
           and not request.COOKIES.get('check_user_loggedin') \
           and not request.path.startswith(redirection):
            if hasattr(settings, 'APP_TAB'):
                loading_message = settings.FACEBOOK_CANVAS_LOADING_MESSAGE
            else:
                loading_message = FACEBOOK_CANVAS_LOADING_MESSAGE
            return HttpResponse(render_to_string('redirect.html',
                                {'redirection': redirection,
                                 'loading_message': loading_message}))

        if request.path.startswith('/accounts/profile'):
            login_referer = request.COOKIES.get('login_referer')
            if not login_referer or 'page_proxy.php' in login_referer:
                login_referer = settings.APP_TAB

            response = HttpResponseRedirect(login_referer)
            response.delete_cookie('login_referer')
            return response

        return

    def get_redirect_uri(self, request, exception):
        """
        Handles the redirections in case the user cancelled the  \
        authentication approval.
        :param request: Django request object.
        :type item: obj
        :param exception: Django exception object.
        :type item: obj
        :returns:  A url to redirect the user to
        :rtype: string
        """
        if hasattr(settings, 'FACEBOOK_CANVAS_APP_TAB') and \
           isinstance(exception, AuthCanceled):
            return settings.FACEBOOK_CANVAS_APP_TAB
        else:
            return super(FacebookCanvasAuth, self) \
                .get_redirect_uri(request, exception)

    def process_response(self, request, response):
        """
        Fixes some issues authenticating via iframe by adding CP HONK to the \
        P3P header.
        :param request: Django request object.
        :type item: obj
        :param exception: Django exception object.
        :type item: obj
        :returns:  A formated django response
        :rtype: obj
        """
        response['P3P'] = 'CP="HONK"'
        return response
