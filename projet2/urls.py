from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', RedirectView.as_view(url='notes/')),
    url(r'^', include('notes.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



urlpatterns += staticfiles_urlpatterns()
