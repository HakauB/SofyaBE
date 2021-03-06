from django.contrib.auth.models import User, Group
from rest_framework import serializers
from fileviewer.models import FileHouse, ActionConfiguration


class UserSerializer(serializers.ModelSerializer):

    filehouses = serializers.HyperlinkedRelatedField(many=True, view_name='filehouse-detail', read_only=True)
    actionconfigurations = serializers.HyperlinkedRelatedField(many=True, view_name='actionconfiguration-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'filehouses')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class FileHouseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = FileHouse
        fields = ('submitted', 'title', 'data', 'filetype', 'owner',)

class ActionConfigurationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ActionConfiguration
        fields = ('action', 'arguments', 'owner',)
