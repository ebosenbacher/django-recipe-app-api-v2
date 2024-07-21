"""
Serializers for the user API view.
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """
        Overriding create method of ModelSerializer so that we can call create_user
        on our model manager.
        Create and return a user with encrypted password.
        """
        return get_user_model().objects.create_user(**validated_data)
