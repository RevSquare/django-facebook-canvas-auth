from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^add-check-user-loggedin$',
        'facebook_canvas_auth.views.add_check_user_loggedin',
        name='add_check_user_loggedin'),
)
