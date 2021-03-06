from datetime import datetime

from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from app.api.diary.serializers import DiaryCreateSerializer, DiaryListSerializer, DiaryUpdateSerializer
from app.model import Process, Partner, Negotiation
from app.model.action import Action
from app.model.day import Day
from app.model.diary import Diary
from app.permissions import IsManager, IsManagerOrReadOnly, NotMediaManager


class DiaryCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryCreateSerializer
    # permission_classes = (IsAuthenticated, IsManager)

    def get_queryset(self):
        return Diary.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        cause = self.request.data['cause']
        negotiation_id = self.request.data['negotiation_id']
        destination_date = self.request.data['destination_date']
        description = self.request.data['description']

        if self.request.data.get('partner_id'):
            partner_id = self.request.data['partner_id']
            instance.partner = Partner.objects.get(id=partner_id)

        elif self.request.data.get('other'):
            instance.other = self.request.data['other']

        instance.moder = self.request.user
        day = Day.objects.get(moder=self.request.user, day_date=datetime.today())
        instance.day = day
        instance.save()
        Process.objects.create(moder=self.request.user, cause=cause, negotiation_id=int(negotiation_id),
                               destination_date=destination_date, description=description)
        Action.objects.create(moder=self.request.user, action=f'diary {instance} created', subject=instance)


class DiaryListMyAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer
    # permission_classes = (IsAuthenticated, IsManager)

    def get_queryset(self):
        d, _ = Day.objects.get_or_create(moder=self.request.user, day_date=datetime.today())
        p = Diary.objects.filter(moder=self.request.user)
        if self.request.GET.get('date'):
            p = p.filter(destination_date=self.request.GET.get('date'))
        return p


class DiaryListTodayAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer
    # permission_classes = (IsAuthenticated, IsManager)

    def get_queryset(self):
        p = Diary.objects.filter(moder=self.request.user, destination_date=datetime.today())
        return p


# class DiaryListByDateAPIView(ListAPIView):
#     serializer_class = DiaryListSerializer
#
#     def get_queryset(self):
#         qs = Diary.objects.all().filter()
#         if self.request.GET.get('date'):
#             qs = qs.filter(moder_id=self.request.GET.get('manager_id'))
#         return qs


class DiaryUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = DiaryUpdateSerializer
    # permission_classes = (IsAuthenticated, IsManagerOrReadOnly)

    def get_queryset(self):
        return Diary.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'diary {instance} updated', subject=instance)


class DiaryDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer
    # permission_classes = (IsAuthenticated, IsManagerOrReadOnly)

    def get_queryset(self):
        return Diary.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'diary {instance} deleted', subject=instance)
        instance.delete()


class DiaryDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = DiaryListSerializer
    # permission_classes = (IsAuthenticated, NotMediaManager)

    def get_queryset(self):
        p = Diary.objects.filter(id=self.kwargs['id'])
        return p
