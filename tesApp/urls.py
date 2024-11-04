from django.urls import path
from . import views

urlpatterns = [
    path('', views.tes_list, name='tes_list'),
    path('scores/', views.scores_tes, name='scores_tes'),
    path('scores_all/', views.result_tes_all, name='result_tes_all'),
    path('<int:pk>/', views.tes_detail, name='tes_detail'),
    path('<int:pk>/take/', views.tes_take, name='tes_take'),
    path('<int:pk>/submit/', views.tes_submit, name='tes_submit'),
]