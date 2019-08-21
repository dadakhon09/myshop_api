from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from app.api.diary.serializers import DiaryListSerializer
from app.api.managers.serializers import ManagerDetailSerializer
from app.api.partner.serializers import PartnerListSerializer
from app.model import Diary, Partner


class ManagerDetailAPIView(RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ManagerDetailSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        user = self.request.user
        if user.is_superuser or user.userprofile.type == 2:
            raise PermissionError
        elif user.userprofile.type == 1:
            raise PermissionError

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            "partner": PartnerListSerializer(Partner.objects.filter(moder=self.request.user), many=True).data,
            "diary": DiaryListSerializer(Diary.objects.filter(moder=self.request.user), many=True).data,
            "moder": serializer.data,
        }
        return Response(data)
