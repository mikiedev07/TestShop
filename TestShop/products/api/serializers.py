from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at', 'category_name', 'tags']

    def get_category_name(self, obj):
        return obj.category_id.name
