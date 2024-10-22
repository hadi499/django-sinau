from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('scores/', scores, name='scores'),
    path('all_scores/', all_scores, name='all_scores'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),   
    path('login/', CustomLoginView.as_view(), name='login'),
    path('book/', include('book.urls')),
    path('quiz/', include('quiz.urls')),
    path('sains/', include('sains.urls')),
    path('pertanyaan/', include('pertanyaan.urls')),
    path('posts/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
