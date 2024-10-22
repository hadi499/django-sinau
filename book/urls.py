from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'), 
    path('<int:book_id>/', views.book_detail, name='book_detail'), 
    path('<int:book_id>/all', views.all_page, name='all_page'), 
    path('page/<int:page_id>/', views.page_detail, name='page_detail'), 
]
