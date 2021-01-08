from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('work/', views.work, name='website-work'),
    path('trust/', views.trust, name='website-trust'),
    path('contact/', views.contact, name='website-contact'),
]