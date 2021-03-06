"""sofya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from fileviewer import views
from rest_framework.schemas import get_schema_view

#admin.autodiscover()

schema_view = get_schema_view(title='Pastebin API')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'filehouses', views.FileHouseViewSet)
router.register(r'actionconfigurations', views.ActionConfigurationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^schema/$', schema_view),
    url(r'^admin/', include(admin.site.urls)),
]
