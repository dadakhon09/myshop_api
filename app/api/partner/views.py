import datetime

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from app.model import Settings
from app.model.action import Action
from app.model.partner import Partner
from app.api.partner.serializers import PartnerCreateSerializer, PartnerListSerializer, PartnerTransferSerializer, \
    PartnerUpdateSerializer
from app.permissions import IsOwnerOrReadOnly, IsMediaManager


class PartnerCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerCreateSerializer

    # def get_permissions(self):
    #     if self.request.user.is_superuser:
    #         return []
<<<<<<< HEAD
    #     elif self.request.user.userprofile.type == 0:
    #         return [IsMediaManager, IsAuthenticated]
    #     elif self.request.user.userprofile.type == 1:
    #         return [IsAuthenticated, ]
=======
    #     if self.request.user.userprofile.type == 0:
    #         return [IsMediaManager, IsAuthenticated]
>>>>>>> ca6a17defe5035c3970f7b70f59ed750dc3b5c93
    
    def perform_create(self, serializer):
        instance = serializer.save()
        print(instance)
        instance.moder = self.request.user
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'partner {instance} created', subject=instance)


class PartnerListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer
    permission_classes = (IsMediaManager, IsAdminUser, IsAuthenticated )

    def get_queryset(self):
        Settings.objects.get_or_create(negotiation_durability=2)
        return Partner.objects.all()


class PartnerListByModerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        p = Partner.objects.filter(moder=self.request.user)
        return p


class PartnerTransferredListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        p = Partner.objects.filter(moder=self.request.user, transferred=True)
        return p


class PartnerDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    def get_queryset(self):
        d = Partner.objects.get(id=self.kwargs['id'])
        p = Partner.objects.filter(id=self.kwargs['id'])
        if self.request.user == d.moder:
            d.transferred = False
            d.save()
        return p


class PartnerTransferAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerTransferSerializer
    # permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Partner.objects.all()


class PartnerUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = PartnerUpdateSerializer

    def get_queryset(self):
        return Partner.objects.all()

    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance)
        instance.save()
        Action.objects.create(moder=self.request.user, action=f'partner {instance} updated ',
                              subject=instance)


class PartnerDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PartnerListSerializer

    # def get_permissions(self):
    #     if self.request.user.is_superuser:
    #         return []
    #     else:
    #         return [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        return Partner.objects.all()

    def perform_destroy(self, instance):
        Action.objects.create(moder=self.request.user, action=f'partner {instance} deleted',
                              subject=instance)
        instance.delete()
