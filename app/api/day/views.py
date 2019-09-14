from datetime import datetime

from django.http import HttpResponse
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.day.serializers import DayCreateSerializer, DayListSerializer, DayUpdateSerializer, DayEndSerializer, \
    DayStartSerializer
from app.api.users.serializers import UserSerializer
from app.model import Diary
from app.model.action import Action
from app.model.day import Day


class DayCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer
    queryset = Day.objects.all()
    # permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} created', subject=instance)


class DayListAllAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayListMyAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(moder=self.request.user)
        return p


class DayUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DayUpdateSerializer

    def get_queryset(self):
        return Day.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} updated', subject=instance)


class DayDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'day {instance} deleted', subject=instance)
        instance.delete()


class DayDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(id=self.kwargs['id'])
        return p


class DayGetStartedAPIView(APIView):
    def post(self, request):

        d = Day.objects.get(moder=self.request.user, day_date=datetime.today())

        if not d.start_time:
            d.start_time = datetime.today()

        day = DayListSerializer(d)
        d.save()

        Action.objects.create(moder=self.request.user, action=f'day {d} started', subject=d)

        return Response(day.data)


class DayGetEndedAPIView(APIView):
    def post(self, request):

        d = Day.objects.get(moder=self.request.user, day_date=datetime.today())

        if d.start_time:
            diaries = Diary.objects.filter(moder=self.request.user, destination_date=datetime.today())

            for p in diaries:
                if p.result == 'None':  # and p.day.day_date == datetime.today().date():
                    return Response('You cant leave now, first finish all your work', status=400)

            d.end_time = datetime.today()
            d.done = True
            day = DayListSerializer(d)
            d.save()

            Action.objects.create(moder=self.request.user, action=f'day {d} ended', subject=d)

            return Response(day.data)

        else:
            return Response('Start your day first', status=400)
