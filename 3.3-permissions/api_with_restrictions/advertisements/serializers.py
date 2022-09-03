from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers


from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at')


    def create(self, validated_data):
        """Метод для создания"""
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)


    # создаем лимит на созданные объекты от пользователя на количество статей
    def validate(self, data):

        stat = data.get('status')
        req = self.context['request'].method

        if req == "POST" or stat == 'OPEN':
            # получаем переменную с нашим пользователем отправившим request (чтобы потом связать объекты именно от этого пользователя)
            user = self.context['request'].user
            # фильтруем объекты по параметру, который нас интересует + убеждаемся, что объекты имменно от пользователся creator=user,
            already_open_offers = Advertisement.objects.filter(creator=user, status="OPEN")
            if already_open_offers.count() > 5:
                raise ValidationError('Вы уже создали 10 открытых объявлений, достигнут лимит!')

        return data
