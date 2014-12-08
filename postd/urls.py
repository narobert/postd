from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   
    url(r'^$', 'userprofile.views.home', name='home'),
    url(r'^dashboard/', 'userprofile.views.dashboard', name='dashboard'),
    url(r'^login/', 'userprofile.views.login'),
    url(r'^logout/', 'userprofile.views.logout'),
    url(r'^register/', 'userprofile.views.register', name='register'),
    url(r'^search/', 'userprofile.views.search', name='search'),
    url(r'^submit/(?P<username>[\w\-]+)', 'userprofile.views.submit', name='submit'),
    url(r'^comment/(?P<id>[\w\-]+)', 'userprofile.views.comment'),
    url(r'^changePic/', 'userprofile.views.changePic', name='changePic'),
    url(r'^upload/(?P<id>[\w\-]+)/$', 'userprofile.views.picture'),
    url(r'^upload/(?P<id>[\w|\W]+)/$', 'userprofile.views.picture'),
    url(r'^user/(?P<username>[\w\-]+)/$', 'userprofile.views.profile'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^ajax/posted/', include('posted.urls')),
)

if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^css/(.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT + "/css", 'show_indexes': True}),
    (r'^images/(.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT + "/images", 'show_indexes': True}),
    (r'^js/(.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT + "/js", 'show_indexes': True}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
      {'document_root': settings.STATIC_ROOT + "/media", 'show_indexes': True}),
  )
