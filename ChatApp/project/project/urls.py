"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include,re_path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from snippets import views
from snippets.views import Login, Registrations, activate, ForgotPassword, reset_password,ResetPassword,session
from django_short_url.views import get_surl
from django_short_url.models import ShortURL
from chatApp.views import message_list, user_list, chat_view, message_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', Login.as_view(), name='index'),
    path('activate/<slug:surl>/', activate, name='activate'),
    path('registration/', Registrations.as_view(), name="registration"),

    path('chat/',chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', message_list, name='message-detail'),  
    path('api/messages/', message_list, name='message-list'),   
    path('api/users/<int:pk>', user_list, name='user-detail'),      
    path('api/users/', user_list, name='user-list'),   
    
    path('forgot_password/', ForgotPassword.as_view(),name="forgot_Password"),
    path('reset_password/<slug:surl>/', reset_password, name="reset_password"),
    path('resetpassword/<user_reset>', ResetPassword.as_view(), name="resetpassword"),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('session/', session),   

]

