from models import Selinux
from rest_framework import viewsets
from serializers import SelinuxSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Selinux.objects.all()
    serializer_class = SelinuxSerializer