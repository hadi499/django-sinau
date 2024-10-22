from django.shortcuts import render
from .models import Pertanyaan

def pertanyaan_view(request):
  posts = Pertanyaan.objects.all()
  return render(request, 'pertanyaan/index.html', {'posts': posts})
