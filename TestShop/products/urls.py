from django.urls import path

from .views import CategoryListAPIView, ProductExportView

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='products'),
    path('export/', ProductExportView.as_view(), name='excel-export')
]
