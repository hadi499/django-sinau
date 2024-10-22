from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
  title = models.CharField(max_length=255)
  image_satu = models.ImageField(upload_to='posts/', null=True, blank=True)
  content_satu = CKEditor5Field(blank=True, null=True)
  image_dua = models.ImageField(upload_to='posts/', null=True, blank=True)
  content_dua = CKEditor5Field(blank=True, null=True)
  image_tiga = models.ImageField(upload_to='posts/', null=True, blank=True)
  content_tiga = CKEditor5Field(blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
