from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Pertanyaan
import os

@receiver(pre_delete, sender=Pertanyaan)
def delete_posts_image(sender, instance, **kwargs):
    if instance.image_question:
        if os.path.isfile(instance.image_question.path):
            os.remove(instance.image_question.path)

    if instance.image_answer:
        if os.path.isfile(instance.image_answer.path):
            os.remove(instance.image_answer.path)



@receiver(pre_save, sender=Pertanyaan)
def delete_old_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    
    try:
        old_instance = Pertanyaan.objects.get(pk=instance.pk)
    except Pertanyaan.DoesNotExist:
        return False

    if old_instance.image_question != instance.image_question:
        if old_instance.image_question:
            if os.path.isfile(old_instance.image_question.path):
                os.remove(old_instance.image_question.path)

    if old_instance.image_answer != instance.image_answer:
        if old_instance.image_answer:
            if os.path.isfile(old_instance.image_answer.path):
                os.remove(old_instance.image_answer.path)