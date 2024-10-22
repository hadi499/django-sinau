from django.urls import path
from . import views

urlpatterns = [
    path('', views.pertanyaan_view, name='pertanyaan'),
]
