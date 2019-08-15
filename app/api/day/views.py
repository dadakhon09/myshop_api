from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.api.day.serializers import DayCreateSerializer, DayListSerializer, DayUpdateSerializer
from app.model.day import Day


class DayCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer
    queryset = Day.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        print(instance)
        instance.moder = self.request.user
        instance.save()


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


class DayDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(id=self.kwargs['id'])
        return p
