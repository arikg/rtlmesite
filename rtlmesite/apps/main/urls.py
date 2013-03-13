from django.conf.urls import patterns, url
from django.views.generic import DetailView, RedirectView
from models import Result

import views

urlpatterns = patterns('',
                       # ex: /favicon.ico
                       url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
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
)