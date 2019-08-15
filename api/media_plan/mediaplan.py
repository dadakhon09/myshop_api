from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.media_plan.serializers import MediaPlanCreateSerializer, MediaPlanListSerializer, MediaPlanUpdateSerializer
from api.models import MediaPlan


class MediaPlanCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanCreateSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanUpdateSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPLanDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        p = MediaPlan.objects.filter(id=self.kwargs['id'])
        return p

