# coding=utf-8

from django.conf.urls import include, url
from views import *
from product import *

urlpatterns = [
url('^import_data/$', ImportDataView.as_view(), name='import_data'),
url('^host_list/$', HostListView.as_view(), name='host_list'),
url('^host_edit/(?P<pk>\d+)?/?$', HostEditView.as_view(), name='host_edit'),
url('^product_detail/(?P<pk>\d+)?/?$', ProductDetailView.as_view(), name='product_detail'),
url('^product_add/$', ProductAddView.as_view(), name='product_add'),
]

