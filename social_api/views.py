from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from . import models, permissions, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating UserProfile."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
