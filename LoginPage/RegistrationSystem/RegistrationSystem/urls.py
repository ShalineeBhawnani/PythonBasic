from django.conf.urls import url
from django.contrib import admin
from loginpage.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',login,name='login'),
]
