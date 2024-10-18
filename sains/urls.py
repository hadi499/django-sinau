from django.urls import path
from . import views

urlpatterns = [
    path('', views.sains_list, name='sains_list'),
    path('scores/', views.scores_sains, name='scores_sains'),
    path('<int:pk>/', views.sains_detail, name='sains_detail'),
    path('<int:pk>/take/', views.sains_take, name='sains_take'),
    path('<int:pk>/submit/', views.sains_submit, name='sains_submit'),
]