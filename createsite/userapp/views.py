from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]