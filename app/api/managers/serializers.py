from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class userFullSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

