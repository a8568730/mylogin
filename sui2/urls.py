from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^新增一個使用者$', 新增一個使用者, name='新增一個使用者')
)