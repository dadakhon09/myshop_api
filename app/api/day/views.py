import datetime

from django.http import HttpResponse
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.day.serializers import DayCreateSerializer, DayListSerializer, DayUpdateSerializer, DayEndSerializer, \
    DayStartSerializer
from app.model import Diary
from app.model.action import Action
from app.model.day import Day


class DayCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DayCreateSerializer
    queryset = Day.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} created', subject=instance)


class DayListByIdAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        return Day.objects.all()


class DayListByModerAPIView(ListAPIView):
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

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} deleted', subject=instance)


class DayDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DayListSerializer

    def get_queryset(self):
        p = Day.objects.filter(id=self.kwargs['id'])
        return p


class DayGetStartedAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DayStartSerializer
    queryset = Day.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.start_time = datetime.datetime.now()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} started', subject=instance)


class DayGetEndedAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DayEndSerializer
    queryset = Day.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        diaries = Diary.objects.filter(moder=self.request.user)
        for d in diaries:
            if d.result is None and d.day.day_date == datetime.datetime.today().date():

                return Response(status=400)
        instance.end_time = datetime.datetime.now()
        instance.done = True
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'day {instance} ended', subject=instance)
