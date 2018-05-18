# _*_ coding: utf-8 _*_
from django.conf.urls import url
from .views import *

urlpatterns = [
    # url('^apply/$', ApplyView.as_view(), name='apply'),
    # url('^apply_list/$', ApplyListView.as_view(), name='apply_list'),
    # url('^deploy/(?P<pk>[0-9]+)?/$',  DeployView.as_view(), name='deploy'),
    # url('^deploy_history/$', DeployHistoryView.as_view(), name='deploy_history'),
    url('^build/$', BuildView.as_view(), name='build'),
    # url('^edit/(?P<pk>[0-9]+)?$', JsonfileEditView.as_view(), name='edit'),
    url('^result/(?P<jobname>.+)?$', BuildresultView.as_view(), name='result'),
    url('^edit/(?P<jobname>.*)?$', JsonfileEditView.as_view(), name='edit'),
    url('^console/$', Jenkins_console_out_view.as_view(), name='console'),
    url('^deploy/$', DeploydcosView.as_view(), name='deploy'),
    url('^deployapp/(?P<jobname>.*)?$', DeployappView.as_view(), name='deployapp'),
    url('^dcosapp/(?P<jobname>.*)?$', Dcosappview.as_view(), name='dcosapp'),

    # 获取某个项目的所有标签(版本)
    # url('^get_project_versions/$', GetProjectVersionsView.as_view(), name='get_project_versions'),
]