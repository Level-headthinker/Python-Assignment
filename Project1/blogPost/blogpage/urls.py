from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Listpage, name='Listpage'),
    path('create/', views.blogpage, name='blogpage'),
    path('<int:blog_id>/', views.detailpage, name='detailpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
