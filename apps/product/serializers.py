from rest_framework import serializers
from .models import Product, ProductImage, Category


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return price

    def validate_quantity(self, quantity):
        if quantity < 0:
            raise serializers.ValidationError('Количество не может быть отрицательным')
        return quantity
    
    def validate(self, attrs):
        user = self.context['request'].user
        attrs['user'] = user
        return attrs


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('image', 'title', 'price', 'in_stock', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



# {
#     'user': 
#     'title': 123123,
#     'priuce': 12341234
# }