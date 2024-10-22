from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags

class Pertanyaan(models.Model):
  title = models.CharField(max_length=200, default='title')
  image_question = models.ImageField(upload_to='pertanyaan/', null=True, blank=True)
  question = CKEditor5Field(blank=True, null=True)
  image_answer = models.ImageField(upload_to='pertanyaan/', null=True, blank=True)
  answer = CKEditor5Field(blank=True, null=True)

  def __str__(self):
    return self.title
  


