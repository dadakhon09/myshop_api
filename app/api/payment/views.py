from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from app.model.action import Action
from app.model.payment import Payment
from app.api.payment.serializers import PaymentCreateSerializer, PaymentListSerializer, PaymentUpdateSerializer


class PaymentCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PaymentCreateSerializer
    permission_classes = ()

    def get_queryset(self):
        return Payment.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'payment {instance} created', subject=instance)


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

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'payment {instance} updated', subject=instance)


class PaymentDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        return Payment.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'payment {instance} deleted', subject=instance)


class PaymentDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PaymentListSerializer

    def get_queryset(self):
        p = Payment.objects.filter(id=self.kwargs['id'])
        return p
