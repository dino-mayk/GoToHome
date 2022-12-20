from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>/', views.post_details, name='posts_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
]
