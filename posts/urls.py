from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('post/<int:pk>', views.post, name='post'),
    path('create/', views.create_post, name='create'),
    path('delete/<int:rec_pk>', views.delete_post, name="delete"),
    path('edit/<int:rec_pk>', views.edit_post, name="edit"),
]
