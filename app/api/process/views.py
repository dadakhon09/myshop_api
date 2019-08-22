import datetime

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from app.model import Diary, Negotiation, Partner
from app.model.action import Action
from app.model.day import Day
from app.model.process import Process
from app.api.process.serializers import ProcessCreateSerializer, ProcessListSerializer, ProcessUpdateSerializer
from app.permissions import IsOwnerOrReadOnly

now = datetime.datetime.now()


class ProcessCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessCreateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Process.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        negotiation_id = self.request.data['negotiation_id']
        cause = self.request.data['cause']
        destination_date = self.request.data['destination_date']
        description = self.request.data['description']
        n = Negotiation.objects.get(id=negotiation_id)
        p = Partner.objects.get(id=n.partner_id)
        print(p)
        instance.negotiation = n
        instance.moder = self.request.user
        instance.day = datetime.datetime.today()
        instance.save()
        day = Day.objects.get(moder=self.request.user, day_date=datetime.datetime.today())
        Diary.objects.create(moder=self.request.user, partner_id=int(p.id), destination_date=destination_date,
                             cause=cause, description=description, day=day)
        Action.objects.create(moder=self.request.user, action=f'process {instance} created', subject=instance)


class ProcessTodayListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        p = Process.objects.filter(moder=self.request.user, destination_date=now.today())
        return p


class ProcessListByModerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        p = Process.objects.filter(moder=self.request.user)
        return p


class ProcessAllListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    queryset = Process.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)


class ProcessUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessUpdateSerializer

    def get_queryset(self):
        return Process.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'process {instance} updated', subject=instance)


class ProcessDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        return Process.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'process {instance} deleted', subject=instance)


class ProcessDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        p = Process.objects.filter(id=self.kwargs['id'])
        return p
