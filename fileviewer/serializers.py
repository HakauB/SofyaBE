from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fileviewer.models import FileHouse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class FileHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileHouse
        fields = ('submitted', 'title', 'data', 'filetype')
