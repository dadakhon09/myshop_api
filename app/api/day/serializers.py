from rest_framework.serializers import ModelSerializer

from app.api.users.serializers import UserSerializer
from app.model.day import Day


class DayListSerializer(ModelSerializer):
    moder = UserSerializer()

    class Meta:
        model = Day
        fields = ('id', 'created', 'day_date', 'moder', 'done', 'start_time', 'end_time')


class DayListTodaySerializer(ModelSerializer):
    moder = UserSerializer()

    class Meta:
        model = Day
        fields = ('id', 'moder', 'start_time', 'end_time')


class DayUpdateSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'done', 'start_time', 'end_time')


class DayCreateSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', )


class DayStartSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'start_time')


class DayEndSerializer(ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'day_date', 'done', 'end_time')
