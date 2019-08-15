from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView

from app.model.action import Action
from app.model.partner import Partner
from app.api.partner.serializers import PartnerCreateSerializer, PartnerListSerializer, PartnerTransferSerializer, \
    PartnerUpdateSerializer


class PartnerCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        Action.objects.create(actor=self.request.user, action='partner_create', subject=instance,
                              comment='string')

        instance.save()


class PartnerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer
    queryset = Partner.objects.all().order_by('id')


class PartnerListByModerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        print(self.kwargs)
        p = Partner.objects.filter(moder__username=self.kwargs['slug'])
        return p


class PartnerDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        p = Partner.objects.filter(id=self.kwargs['id'])
        return p


class PartnerTransferAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerTransferSerializer

    def get_queryset(self):
        return Partner.objects.all()


class PartnerUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerUpdateSerializer

    def get_queryset(self):
        return Partner.objects.all()


class PartnerDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        return Partner.objects.all()
