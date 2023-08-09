from rest_framework import serializers
from products.models import Product, Tag


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'
