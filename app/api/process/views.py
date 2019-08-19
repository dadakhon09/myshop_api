import datetime

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from app.model.action import Action
from app.model.process import Process
from app.api.process.serializers import ProcessCreateSerializer, ProcessListSerializer, ProcessUpdateSerializer


now = datetime.datetime.now()


class ProcessCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Process.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'process {instance} created', subject=instance)


class ProcessTodayListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    
    def get_queryset(self):
        p = Process.objects.filter(moder__username=self.kwargs['slug'], destination_date=now.today())
        return p


class ProcessListByModerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        print(self.kwargs)
        p = Process.objects.filter(moder__username=self.kwargs['slug'])
        return p


class ProcessAllListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    queryset = Process.objects.all()


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
