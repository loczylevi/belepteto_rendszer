from django.urls import path

from . import views

urlpatterns = [
    path('', views.fo_oldal, name='fo_oldal')
]
