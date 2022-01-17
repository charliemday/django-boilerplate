import ipdb
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=6, write_only=True, required=True)

    def validate(self, data):
        username = data.get("username")
        if username:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                raise serializers.ValidationError("That username is already in use")
        return data

    def create(self, validated_data):
        # For creating users we must hash their password before storing
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"
