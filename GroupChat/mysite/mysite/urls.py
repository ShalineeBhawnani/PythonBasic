from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from snippets.views import Login, Registrations, activate, ForgotPassword
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from chat.views import index, room
# mysite/urls.py
from django.conf.urls import include

  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', Login.as_view(), name='login'),
    path('activate/<slug:surl>/', activate, name='activate'),
    path('registration/', Registrations.as_view(), name="registration"),
    path('forgotpassword/', ForgotPassword.as_view(),name="forgotPassword"),
    # path('activate/<surl>/', views.activate, name="activate"),
    path('chat/', include('chat.urls')),
    # path('index', index, name='index'),
    # path('<str:room_name>/', room, name='room'),

]