from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.action.serializers import ActionCreateSerializer, ActionListSerializer, ActionUpdateSerializer
from api.models import Action


class ActionCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ActionCreateSerializer
    queryset = Action.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.actor = self.request.user
        instance.save()


class ActionListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    queryset = Action.objects.all()


class ActionUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ActionUpdateSerializer

    def get_queryset(self):
        return Action.objects.all()


class ActionDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer

    def get_queryset(self):
        return Action.objects.all()


class ActionDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer

    def get_queryset(self):
        p = Action.objects.filter(id=self.kwargs['id'])
        return p
