from django.urls import path

from chat import views

urlpatterns = [
  path('', views.index, name='index'),
  path('/', views.room, name='room'),
]
