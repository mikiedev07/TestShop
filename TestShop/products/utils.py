from openpyxl import Workbook

from .models import Product


def excel_creation():
    wb = Workbook()
    ws = wb.active

    columns = ['id', 'category', 'tags', 'name', 'description', 'price', 'created_at']
    ws.append(columns)

    queryset = Product.objects.select_related('category_id').prefetch_related('tags').only(
        'id',
        'name',
        'description',
        'price',
        'created_at',
        'category_id__name',
        'tags__name',
    )
    for obj in queryset:
        category = obj.category_id.name
        tags = ', '.join([tag.name for tag in obj.tags.all()])
        row = [obj.id, category, tags, obj.name, obj.description, obj.price, str(obj.created_at)]
        ws.append(row)

    return wb
