from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='index'),
    path('about/', views.about, name='sobre mi'),
    path('services/', views.services, name='servicios'),
    path('store/', views.store, name='tienda'),
    path('contact/', views.contact, name='contacto'),
    path('blog/', views.blog, name='blog'),
]
