from django.contrib import admin
from django.urls import path, include
from posts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),

    # Auth
    path('log_in/', views.login, name='log_in'),
    path('singup', views.signup, name='singup'),
    path('logout/', views.log_out, name='logout'),
]
