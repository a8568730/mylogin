from django.conf.urls import patterns, url
from sui2.介面_後臺 import 新增一個使用者
from sui2.介面_後臺 import 顯示所有使用者


urlpatterns = patterns('',
    url(r'^新增一個使用者$', 新增一個使用者, name='新增一個使用者'),
    url(r'^顯示所有使用者$', 顯示所有使用者, name='顯示所有使用者'),
    url(r'^$', 新增一個使用者, name='新增一個使用者')
)