from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Page
import os

@receiver(pre_delete, sender=Page)
def delete_page_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(pre_save, sender=Page)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_instance = Page.objects.get(pk=instance.pk)
    except Page.DoesNotExist:
        return False

    if old_instance.image != instance.image:
        if old_instance.image:
            if os.path.isfile(old_instance.image.path):
                os.remove(old_instance.image.path)