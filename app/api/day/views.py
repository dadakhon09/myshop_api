import datetime

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
    # lookup_field = 'pk'
    # serializer_class = DayStartSerializer

    # def get_queryset(self):
    #     return Day.objects.filter(moder=self.request.user)
    #
    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     instance.start_time = datetime.datetime.now()
    #
    #     instance.save()
    #     Action.objects.create(moder=self.request.user, action=f'day {instance} started', subject=instance)

    def post(self, request):
        d = Day.objects.get(moder=self.request.user, day_date=datetime.datetime.today())
        d.start_time = datetime.datetime.today()
        moder = UserSerializer(self.request.user)
        day = DayListSerializer(d)
        d.save()

        # qs = self.get_queryset()
        # page = self.paginate_queryset(qs)
        # serializer = self.get_serializer(page, many=True)
        #
        # return self.get_paginated_response(serializer.data)

        Action.objects.create(moder=self.request.user, action=f'day {d} started', subject=d)

        return Response(day.data)


class DayGetEndedAPIView(APIView):
    # lookup_field = 'pk'
    # serializer_class = DayEndSerializer
    #
    # def get_queryset(self):
    #     return Day.objects.filter(moder=self.request.user)
    #
    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     diaries = Diary.objects.filter(moder=self.request.user)
    #     for d in diaries:
    #         if d.result is None and d.day.day_date == datetime.datetime.today().date():
    #             return Response(status=400)
    #     instance.end_time = datetime.datetime.now()
    #     instance.done = True
    #     instance.save()
    #     Action.objects.create(moder=self.request.user, action=f'day {instance} ended', subject=instance)

    def post(self, request):
        d = Day.objects.get(moder=self.request.user, day_date=datetime.datetime.today())
        diaries = Diary.objects.filter(moder=self.request.user)
        for p in diaries:
            if p.result is None and p.day.day_date == datetime.datetime.today().date():
                return Response(status=400)
        moder = UserSerializer(self.request.user)
        d.end_time = datetime.datetime.today()
        d.done = True
        day = DayListSerializer(d)
        d.save()

        # qs = self.get_queryset()
        # page = self.paginate_queryset(qs)
        # serializer = self.get_serializer(page, many=True)
        #
        # return self.get_paginated_response(serializer.data)

        Action.objects.create(moder=self.request.user, action=f'day {d} ended', subject=d)

        return Response(day.data)
