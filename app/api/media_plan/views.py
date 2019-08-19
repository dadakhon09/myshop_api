from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.api.media_plan.serializers import MediaPlanCreateSerializer, MediaPlanListSerializer, MediaPlanUpdateSerializer
from app.model.action import Action
from app.model.media_plan import MediaPlan


class MediaPlanCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return MediaPlan.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} created', subject=instance)


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

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} updated', subject=instance)


class MediaPlanDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        return MediaPlan.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} deleted', subject=instance)


class MediaPLanDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer

    def get_queryset(self):
        p = MediaPlan.objects.filter(id=self.kwargs['id'])
        return p

