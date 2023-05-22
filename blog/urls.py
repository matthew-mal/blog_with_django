from django.contrib import admin
from django.urls import path, include
from posts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('posts.urls')),

                  # Auth
                  path('log_in/', views.log_in, name='log_in'),
                  path('singup', views.signup, name='singup'),
                  path('logout/', views.log_out, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
