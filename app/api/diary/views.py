from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.api.diary.serializers import DiaryCreateSerializer, DiaryListSerializer, DiaryUpdateSerializer
from app.model import Process
from app.model.action import Action
from app.model.diary import Diary


class DiaryCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer
    permission_classes = ()

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
        return Diary.objects.all()


class DiaryListByModerAPIView(ListAPIView, CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        p = Diary.objects.filter(moder__username=self.kwargs['slug'])
        return p

    # def perform_create(self, serializer):
    #     d = Day.objects.get_or_create(moder__username=self.kwargs['slug'])
    #     return d


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
