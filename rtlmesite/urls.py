from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

from tastypie.api import Api
from apps.main.api.resources import ResultResource

v1_api = Api(api_name='v1')
v1_api.register(ResultResource())

urlpatterns = patterns('',
                       # ex: /favicon.ico
                       url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
                       # Examples:
                       # url(r'^$', 'rtlmesite.views.home', name='home'),
                       # url(r'^rtlmesite/', include('rtlmesite.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^', include('rtlmesite.apps.main.urls', namespace="main")),
                       )
