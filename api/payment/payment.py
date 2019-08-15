from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from api.models import Payment
from api.payment.serializers import PaymentCreateSerializer, PaymentListSerializer, PaymentUpdateSerializer


class PaymentCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentCreateSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentUpdateSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()


class PaymentDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        p = Payment.objects.filter(id=self.kwargs['id'])
        return p
