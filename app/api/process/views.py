from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from app.model.process import Process
from app.api.process.serializers import ProcessCreateSerializer, ProcessListSerializer, ProcessUpdateSerializer


class ProcessCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessCreateSerializer


class ProcessListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer
    queryset = Process.objects.all()


class ProcessUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ProcessUpdateSerializer

    def get_queryset(self):
        return Process.objects.all()


class ProcessDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        return Process.objects.all()


class ProcessDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ProcessListSerializer

    def get_queryset(self):
        p = Process.objects.filter(id=self.kwargs['id'])
        return p
