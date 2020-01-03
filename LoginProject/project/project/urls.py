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
from django.urls import path,include,re_path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from snippets import views
from snippets.views import Login, Registrations, activate
from django_short_url.views import get_surl
from django_short_url.models import ShortURL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token), 
    path('api/token/', obtain_jwt_token), 
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Registrations.as_view(), name='registration'),
    path('activate/<slug:surl>/', views.activate, name='activate'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate_account, name='activate')
    #     (?P<surl>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$
    # (?P<surl>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$
]

