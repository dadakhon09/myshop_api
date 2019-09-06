from collections import OrderedDict

from django.contrib.auth.models import User
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer

from app.model import Partner, Diary
from app.model.users import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'type')


class UserFullSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username')

    def to_representation(self, instance):
        from app.api.partner.serializers import PartnerListSerializer
        from app.api.diary.serializers import DiaryListSerializer
        ret = super(UserFullSerializer, self).to_representation(instance)
        p = Partner.objects.filter(moder__username=ret.get('username'))
        ps = PartnerListSerializer(p, many=True)
        d = Diary.objects.filter(moder__username=ret.get('username'))
        ds = DiaryListSerializer(d, many=True)
        ret['partner'] = ps.data
        ret['diary'] = ds.data
        return ret
