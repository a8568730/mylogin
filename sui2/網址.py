from django.conf.urls import patterns, url
from sui2.介面_後臺 import 新增一個使用者


urlpatterns = patterns('',
    url(r'^新增一個使用者$', 新增一個使用者, name='新增一個使用者')
    #url(r'^$', views.index, name='index'),
)