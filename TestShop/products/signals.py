from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Product


@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def product_change_handler(sender, instance, **kwargs):
    print('------- CACHE DELETED -------')
    cache.clear()
