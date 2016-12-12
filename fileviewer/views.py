from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from fileviewer.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fileviewer.models import FileHouse
from fileviewer.serializers import FileHouseSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FileHouseList(APIView):
    """
    List all filehouses, or create a new filehouse.
    """
    def get(self, request, format=None):
        filehouses = FileHouse.objects.all()
        serializer = FileHouseSerializer(filehouses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FileHouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileHouseDetail(APIView):
    """
    Retrieve, update or delete a filehouse instance.
    """
    def get_object(self, pk):
        try:
            return FileHouse.objects.get(pk=pk)
        except FileHouse.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        filehouse = self.get_object(pk)
        serializer = FileHouseSerializer(filehouse)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        filehouse = self.get_object(pk)
        serializer = FileHouseSerializer(filehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        filehouse = self.get_object(pk)
        filehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
