from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.model.negotiation import Negotiation
from app.api.negotiation.serializers import NegotiationCreateSerializer, NegotiationListSerializer, \
    NegotiationUpdateSerializer


class NegotiationCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationCreateSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


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


class NegotiationDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        return Negotiation.objects.all()


class NegotiationDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = NegotiationListSerializer

    def get_queryset(self):
        p = Negotiation.objects.filter(id=self.kwargs['id'])
        return p
