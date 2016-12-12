from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fileviewer.models import FileHouse


class UserSerializer(serializers.ModelSerializer):

    filehouses = serializers.PrimaryKeyRelatedField(many=True, queryset=FileHouse.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'filehouses')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class FileHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileHouse
        fields = ('submitted', 'title', 'data', 'filetype')
