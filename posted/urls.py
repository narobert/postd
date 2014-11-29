from django.conf.urls import patterns, include, url

urlpatterns = patterns(

    'posted.views',

    (r'picture$', 'picture'),
    (r'getProfile$', 'getProfile'),
    (r'firstLook$', 'firstLook'),
    (r'accept$', 'accept'),
    (r'reject$', 'reject'),
    (r'load$', 'load'),
    (r'everyone$', 'everyone'),
    (r'delete$', 'delete')

)
