from rest_framework import serializers
from django.db import models
from .models import Product, Stock, StockProduct



class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'stocks']


class ProductPositionSerializer(serializers.ModelSerializer):


    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']




class StockSerializer(serializers.ModelSerializer):
    # positions = ProductPositionSerializer(many=True, queryset=StockProduct.objects.all())
    positions = ProductPositionSerializer(many=True)


    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']




    def create(self, validated_data):
        pos_data = validated_data.pop('positions')
        stock = super().create(validated_data)

        for position in pos_data:
            StockProduct.objects.create(stock=stock, **position)
        return stock



    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for pos in positions:
            StockProduct.objects.update_or_create(defaults={'quantity': pos['quantity'], 'price': pos['price']},
                stock=stock, product=pos['product'])
        return stock





    #
    # def update(self, instance, validated_data):
    #     # достаем связанные данные для других таблиц
    #     positions = validated_data.pop('positions')
    #
    #     # обновляем склад по его параметрам
    #     stock = super().update(instance, validated_data)
    #
    #     # здесь вам надо обновить связанные таблицы
    #     # в нашем случае: таблицу StockProduct
    #     # с помощью списка positions
    #
    #     return stock
    #