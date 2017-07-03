from django.conf.urls import url, include
from django.contrib import admin
from gestionDesRestos import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]
