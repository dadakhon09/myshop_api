from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.diary.serializers import DiaryCreateSerializer, DiaryListSerializer, DiaryUpdateSerializer
from api.models import Diary


class DiaryCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer

    def get_queryset(self):
        return Diary.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()


class DiaryListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryUpdateSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        return Diary.objects.all()


class DiaryDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer

    def get_queryset(self):
        p = Diary.objects.filter(id=self.kwargs['id'])
        return p
