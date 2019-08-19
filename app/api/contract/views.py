from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView

from app.api.contract.serializers import ContractCreateSerializer, ContractListSerializer, ContractUpdateSerializer
from app.model.action import Action
from app.model.contract import Contract


class ContractCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ContractCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Contract.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'contract {instance} created', subject=instance)


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

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'contract {instance} updated ', subject=instance)


class ContractDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'contract {instance} deleted', subject=instance)
        return instance


class ContractDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ContractListSerializer

    def get_queryset(self):
        p = Contract.objects.filter(id=self.kwargs['id'])
        return p
