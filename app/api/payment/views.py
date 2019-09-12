from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.model.action import Action
from app.model.payment import Payment
from app.api.payment.serializers import PaymentCreateSerializer, PaymentListSerializer, PaymentUpdateSerializer


class PaymentCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentCreateSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Payment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        p = Payment.objects.get(id=serializer.data['id'])
        data = {
            "id": serializer.data['id'],
            "contract": serializer.data['contract'],
            "cash": serializer.data['cash'],
            "pay_day": serializer.data['pay_day'],
            "paid": p.contract.paid(),
            "debt": p.contract.debt()
        }
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentUpdateSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'payment {instance} updated', subject=instance)


class PaymentListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'payment {instance} deleted', subject=instance)
        instance.delete()


class PaymentDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        p = Payment.objects.filter(id=self.kwargs['id'])
        return p
