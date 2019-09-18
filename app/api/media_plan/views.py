from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.api.media_plan.serializers import MediaPlanCreateSerializer, MediaPlanListSerializer, MediaPlanUpdateSerializer
from app.model.action import Action
from app.model.media_plan import MediaPlan, Document
from app.model.contract import Contract
from app.permissions import IsMediaManager, IsMediaManagerOrReadOnly


class MediaPlanCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanCreateSerializer
    permission_classes = (IsAuthenticated, IsMediaManager)

    def get_queryset(self):
        return MediaPlan.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} created', subject=instance)


class MediaPlanListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer
    permission_classes = (IsAuthenticated, IsMediaManagerOrReadOnly)

    def get_queryset(self):
        return MediaPlan.objects.all()


class MediaPlanUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanUpdateSerializer
    permission_classes = (IsAuthenticated, IsMediaManagerOrReadOnly)

    def get_queryset(self):
        return MediaPlan.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} updated', subject=instance)


class MediaPlanDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer
    permission_classes = (IsAuthenticated, IsMediaManagerOrReadOnly)

    def get_queryset(self):
        return MediaPlan.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'media plan {instance} deleted', subject=instance)
        instance.delete()


class MediaPLanDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = MediaPlanListSerializer
    permission_classes = (IsAuthenticated, IsMediaManagerOrReadOnly)

    def get_queryset(self):
        p = MediaPlan.objects.filter(id=self.kwargs['id'])
        return p

