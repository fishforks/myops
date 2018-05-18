# _*_ coding: utf-8 _*_
from django.conf.urls import url
from .views import BuildView,BuildresultView,JsonfileEditView,Jenkins_console_out_view,DeploydcosView,DeployappView,Dcosappview

urlpatterns = [
    url('^build/$', BuildView.as_view(), name='build'),
    url('^result/(?P<jobname>.+)?$', BuildresultView.as_view(), name='result'),
    url('^edit/(?P<jobname>.*)?$', JsonfileEditView.as_view(), name='edit'),
    url('^console/$', Jenkins_console_out_view.as_view(), name='console'),
    url('^deploy/$', DeploydcosView.as_view(), name='deploy'),
    url('^deployapp/(?P<jobname>.*)?$', DeployappView.as_view(), name='deployapp'),
    url('^dcosapp/(?P<jobname>.*)?$', Dcosappview.as_view(), name='dcosapp'),

]
