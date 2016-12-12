from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fileviewer import views

urlpatterns = [
    url(r'^filehouse/$', views.FileHouseList.as_view()),
    url(r'^filehouse/(?P<pk>[0-9]+)/$', views.FileHouseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
