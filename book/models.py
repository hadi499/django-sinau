from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Book(models.Model):
  title = models.CharField(max_length=255) 

  def __str__(self):
    return self.title
  

class Page(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  excerpt = models.CharField(max_length=255, help_text="untuk keterangan halaman") 
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  english = CKEditor5Field(blank=True, null=True)
  indonesian = CKEditor5Field(blank=True, null=True)

  def __str__(self):    
    return f'{self.book.title} - {self.excerpt}'