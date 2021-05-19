from django.contrib import admin
from django.urls import path
from game import views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('detail/<int:pk>',views.gamingPost,name='game_details'),
    path('register/',user_view.register,name='register'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
