from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from app.model.action import Action
from app.model.partner import Partner
from app.api.partner.serializers import PartnerCreateSerializer, PartnerListSerializer, PartnerTransferSerializer, \
    PartnerUpdateSerializer
from app.permissions import IsOwnerOrReadOnly


class PartnerCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerCreateSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'partner {instance} created', subject=instance)


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

    def perform_create(self, serializer):
        instance = serializer.save()
        partner = Partner.objects.get(id=instance.data.get("partner"))
        Action.objects.create(actor=self.request.user,
                              action=f'partner {partner} transferred to user {User.objects.get(id=instance.data.get("user_id"))}',
                              subject=partner)


class PartnerUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def get_queryset(self):
        return Partner.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.save()
        Action.objects.create(actor=self.request.user, action=f'partner {instance} updated ',
                              subject=instance)


class PartnerDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        return Partner.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(actor=self.request.user, action=f'partner {instance} deleted',
                              subject=instance)
        return instance
