from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from app.api.diary.serializers import DiaryListSerializer
from app.api.managers.serializers import ManagerDetailSerializer
from app.api.partner.serializers import PartnerListSerializer
from app.api.users.serializers import UserFullSerializer, UserSerializer
from app.model import Diary, Partner


class ManagerDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ManagerDetailSerializer
    queryset = User.objects.filter(userprofile__type__exact=1)
    permission_classes = (IsAdminUser, )

    # def get_permissions(self):
    #     user = self.request.user
    #     if user.userprofile.type == 1:
    #         raise PermissionError

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
    serializer_class = UserFullSerializer
    queryset = User.objects.filter(userprofile__type__exact=0)
    permission_classes = (IsAdminUser, )


class MediaManagerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.filter(userprofile__type__exact=0)


class ManagerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects.filter(userprofile__type__exact=1)
