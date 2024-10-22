from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Post
import os

@receiver(pre_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image_satu:
        if os.path.isfile(instance.image_satu.path):
            os.remove(instance.image_satu.path)

    if instance.image_dua:
        if os.path.isfile(instance.image_dua.path):
            os.remove(instance.image_dua.path)

    if instance.image_tiga:
        if os.path.isfile(instance.image_tiga.path):
            os.remove(instance.image_tiga.path)

@receiver(pre_save, sender=Post)
def delete_old_post_image(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_instance = Post.objects.get(pk=instance.pk)
    except Post.DoesNotExist:
        return False

    if old_instance.image_satu != instance.image_satu:
        if old_instance.image_satu:
            if os.path.isfile(old_instance.image_satu.path):
                os.remove(old_instance.image_satu.path)

    if old_instance.image_dua != instance.image_dua:
        if old_instance.image_dua:
            if os.path.isfile(old_instance.image_dua.path):
                os.remove(old_instance.image_dua.path)

    if old_instance.image_tiga != instance.image_tiga:
        if old_instance.image_tiga:
            if os.path.isfile(old_instance.image_tiga.path):
                os.remove(old_instance.image_tiga.path)