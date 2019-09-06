from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from app.api.diary.serializers import DiaryListSerializer
from app.api.managers.serializers import userFullSerializer
from app.api.partner.serializers import PartnerListSerializer
from app.api.users.serializers import UserFullSerializer, UserSerializer
from app.model import Diary, Partner


class Abc(ListAPIView):

    def get_serializer_context(self):
        context = {
            'request': self.request
        }
        return context

    def get_additional_info(self):
        qs = self.get_queryset()
        print(qs)
        serializer = self.get_serializer(qs, many=True)
        for user in qs:
            data = {
                "moder": serializer.data,
                "partner": PartnerListSerializer(Partner.objects.filter(moder=user), many=True).data,
                "diary": DiaryListSerializer(Diary.objects.filter(moder=user), many=True).data,
            }
        return Response(serializer.data)


class ManagerDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.filter(userprofile__type__exact=1)
    permission_classes = (IsAdminUser, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            "moder": serializer.data,
            "partner": PartnerListSerializer(Partner.objects.filter(moder=self.request.user), many=True).data,
            "diary": DiaryListSerializer(Diary.objects.filter(moder=self.request.user), many=True).data,
        }
        return Response(data)


class MediaManagerDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = userFullSerializer
    queryset = User.objects.filter(userprofile__type__exact=0)
    permission_classes = (IsAdminUser, )


class MediaManagerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = userFullSerializer
    queryset = User.objects.filter(userprofile__type__exact=0)


class ManagerListAPIView(Abc):
    serializer_class = UserFullSerializer
    queryset = User.objects.filter(userprofile__type__exact=1)

    def get(self, request, *args, **kwargs):
        return self.get_additional_info()

    def get_serializer_context(self):
        context = {
            'request': self.request
        }
        return context

