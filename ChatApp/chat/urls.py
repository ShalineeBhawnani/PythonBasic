from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from rest_framework_jwt.views import obtain_jwt_token
from django_short_url.views import get_surl
from django_short_url.models import ShortURL


urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', views.message_view, name='chat'),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    path('api/users', views.user_list, name='user-list'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('register', views.register_view, name='register'),
]