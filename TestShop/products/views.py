from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from openpyxl import Workbook

from .models import Product
from .api.serializers import ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductExportView(APIView):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

        wb = Workbook()
        ws = wb.active

        columns = ['id', 'category_id', 'tags', 'name', 'description', 'price', 'created_at']
        ws.append(columns)

        queryset = Product.objects.all()
        for obj in queryset:
            row = [obj.id, obj.category_id, obj.tags, obj.name, obj.description, obj.price, obj.created_at]
            ws.append(row)

        wb.save(response)
        return response
