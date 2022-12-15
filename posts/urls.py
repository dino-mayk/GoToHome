from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>/', views.post_details, name='posts_detail'),
    path('add_post/', views.add_post, name='add_post'),
]
