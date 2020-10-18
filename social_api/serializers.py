from rest_framework import serializers

from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile object."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Returns a new user by overriding the base class method."""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user

    def update(self, instance, validated_data):
        """Handles updating UserProfile."""

        # Hash the password before updating.
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
