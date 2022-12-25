import time

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Fin_App.models import CustomUser, Space, Shit
from Fin_App.serializers import UsersSerializer, SpaceSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer


class SpaceViewSet(viewsets.ModelViewSet):
    queryset = Space.objects.all()
    serializer_class = SpaceSerializers



@api_view(["GET"])
def health_check(request):
    time.sleep(1)
    return Response({"status": "Ok"}, status.HTTP_200_OK)