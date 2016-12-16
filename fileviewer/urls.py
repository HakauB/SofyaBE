from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fileviewer import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

filehouse_list = FileHouseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
filehouse_detail = FileHouseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
actionconfigurations_list = ActionConfigurationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
actionconfigurations_detail = ActionConfigurationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^filehouse/$', filehouse_list, name='filehouse-list'),
    url(r'^filehouse/(?P<pk>[0-9]+)/$', filehouse_detail, name='filehouse-detail'),
    url(r'^actionconfigurations/$', actionconfigurations_list, name='actionconfigurations-list'),
    url(r'^actionconfigurations/(?P<pk>[0-9]+)/$', actionconfigurations_detail, name='actionconfigurations-detail'),
    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
