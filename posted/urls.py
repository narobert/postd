from django.conf.urls import patterns, include, url

urlpatterns = patterns(

    'posted.views',

    (r'picture$', 'picture'),
    (r'delete$', 'delete')

)
