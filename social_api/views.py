from rest_framework import viewsets

from . import models, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating UserProfile."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
