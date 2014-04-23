import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def add_check_user_loggedin(request):
    max_age = 365*24*60*60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow()
                                         + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")

    response = HttpResponseRedirect(reverse('socialauth_begin',
                                    args=('facebook',)))
    response.set_cookie('check_user_loggedin', 'True', max_age=max_age,
                        expires=expires)
    return response
