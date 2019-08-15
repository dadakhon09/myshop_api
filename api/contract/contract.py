from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from api.contract.serializers import ContractCreateSerializer, ContractListSerializer, ContractUpdateSerializer
from api.models import Contract


class ContractCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ContractCreateSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ContractUpdateSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ContractDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        p = Contract.objects.filter(id=self.kwargs['id'])
        return p
