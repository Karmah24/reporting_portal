from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('verify', views.verify, name = 'verify'),
    path('faq', views.faq, name = 'faq')
]