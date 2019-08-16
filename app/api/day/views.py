from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.api.day.serializers import DayCreateSerializer, DayListSerializer, DayUpdateSerializer
from app.model.action import Action
from app.model.day import Day


class DayCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer
    queryset = Day.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'day {instance} created', subject=instance)


class DayListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DayUpdateSerializer

    def get_queryset(self):
        return Day.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'day {instance} updated', subject=instance)


class DayDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'day {instance} deleted', subject=instance)

class DayDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(id=self.kwargs['id'])
        return p
