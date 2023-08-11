from django.urls import path

from .views import ProductExportView, ProductListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='products'),
    path('export/', ProductExportView.as_view(), name='excel-export'),
]
