from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import *


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user = Users.objects.get(username=username, password=password)
            dt = self.get_serializer_class()(user).data
            return Response({'result': dt}, status=200)

        except:
            return Response({'result': 'user not found'}, status=204)
