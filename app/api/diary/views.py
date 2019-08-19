import datetime

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.api.diary.serializers import DiaryCreateSerializer, DiaryListSerializer, DiaryUpdateSerializer
from app.model.action import Action
from app.model.day import Day
from app.model.diary import Diary


class DiaryCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Diary.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'diary {instance} created', subject=instance)


class DiaryListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        d, _ = Day.objects.get_or_create(moder=self.request.user, day_date=datetime.datetime.today())
        p = Diary.objects.filter(moder=self.request.user)
        return p


# class DiaryListByModerAPIView(ListAPIView):
#     lookup_field = 'id'
#     serializer_class = DiaryListSerializer
#
#     def get_queryset(self):
#         d, _ = Day.objects.get_or_create(moder=self.request.user, day_date=datetime.datetime.today())
#         p = Diary.objects.filter(moder__username=self.kwargs['slug'])
#         return p


class DiaryUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryUpdateSerializer

    def get_queryset(self):
        return Diary.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'diary {instance} updated', subject=instance)


class DiaryDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'diary {instance} deleted', subject=instance)


class DiaryDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        p = Diary.objects.filter(id=self.kwargs['id'])
        return p
