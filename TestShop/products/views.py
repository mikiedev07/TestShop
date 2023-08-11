from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .utils import excel_creation
from .models import Product
from .api.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.select_related('category_id').prefetch_related('tags').only(
        'id',
        'name',
        'description',
        'price',
        'created_at',
        'category_id__name',
        'tags__name',
    )
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60*15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductExportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

        wb = excel_creation()

        wb.save(response)
        return response
