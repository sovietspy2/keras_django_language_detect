from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_predict', views.index, name='get_predict'),
]