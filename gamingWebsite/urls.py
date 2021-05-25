from django.contrib import admin
from django.urls import path
from game import views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('game/action', views.action, name='action'),
                  path('game/action-adventure', views.action_adventure, name='action-adventure'),
                  path('detail/<int:pk>', views.gamingPost, name='game_details'),
                  path('register/', user_view.register, name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='user/login.html'), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
