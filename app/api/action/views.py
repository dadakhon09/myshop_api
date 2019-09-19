from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from app.api.action.serializers import ActionCreateSerializer, ActionListSerializer, ActionUpdateSerializer
from app.model import Partner
from app.model.action import Action


class ActionCreateAPIView(CreateAPIView):
    lookup_field = 'id'
    serializer_class = ActionCreateSerializer
    queryset = Action.objects.all()
    # permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.moder = self.request.user
        instance.save()


class ActionListAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Action.objects.all()

    def get_content_type_for_model(obj):
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level.
        from django.contrib.contenttypes.models import ContentType
        return ContentType.objects.get_for_model(obj, for_concrete_model=False)


class ActionUpdateAPIView(RetrieveUpdateAPIView):
    lookup_field = 'id'
    serializer_class = ActionUpdateSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Action.objects.all()


class ActionDeleteAPIView(RetrieveDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Action.objects.all()


class ActionDetailAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        p = Action.objects.filter(id=self.kwargs['id'])
        return p


class ActionListByManagerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Action.objects.filter(moder__userprofile__type__exact=1)


class ActionListByMediaManagerAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Action.objects.filter(moder__userprofile__type__exact=0)


class ActionListByManagerIdAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Action.objects.filter(moder=self.kwargs['id'], moder__userprofile__type__exact=0)


class ActionListByMediaManagerIdAPIView(ListAPIView):
    lookup_field = 'id'
    serializer_class = ActionListSerializer
    # permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        return Action.objects.filter(moder=self.kwargs['id'], moder__userprofile__type__exact=1)
