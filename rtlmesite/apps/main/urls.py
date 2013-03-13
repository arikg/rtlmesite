from django.conf.urls import patterns, url, handler500
from django.views.generic import DetailView
from models import Result

import views

handler500 = 'views.server_error'

urlpatterns = patterns('',
                       # ex: /
                       url(r'^$', views.index, name='index'),
                       # ex: /result/5/feedback
                       url(r'^result/(?P<result_id>\d+)/feedback/$', views.feedback, name='feedback'),
                       # ex: /result/5/
                       url(r'^result/(?P<pk>\d+)/$',
                           DetailView.as_view(model=Result, template_name='main/result.html'),
                           name="result"),
                       # ex: /rtl
                       url(r'^rtl/$', views.rtl, name='rtl'),
                       # ex: /thanks
                       url(r'^thanks$', views.thanks, name='thanks'),
                       url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to',
                           {'url': '/static/images/favicon.ico'})
)