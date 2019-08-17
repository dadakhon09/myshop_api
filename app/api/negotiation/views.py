from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.model.action import Action
from app.model.negotiation import Negotiation
from app.api.negotiation.serializers import NegotiationCreateSerializer, NegotiationListSerializer, \
    NegotiationUpdateSerializer


class NegotiationCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} created', subject=instance)


class NegotiationListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationUpdateSerializer

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} updated', subject=instance)


class NegotiationDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()

    def perform_destroy(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'negotiation {instance} deleted', subject=instance)


class NegotiationDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        p = Negotiation.objects.filter(id=self.kwargs['id'])
        return p
