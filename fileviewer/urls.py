from django.conf.urls import url
from fileviewer import views

urlpatterns = [
    url(r'^filehouse/$', views.filehouse_list),
    url(r'^filehouse/(?P<pk>[0-9]+)/$', views.filehouse_detail),
]
