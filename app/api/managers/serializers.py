from collections import OrderedDict

from django.contrib.auth.models import User
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer
from rest_framework.utils.serializer_helpers import ReturnDict


class userFullSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
