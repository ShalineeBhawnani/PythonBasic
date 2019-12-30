# from django.conf.urls import url
# from django.contrib import admin
# from loginpage.views import login

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^login/$',login,name='login'),
#     #url(r'^api-auth/', include('rest_framework.urls'))
# ]
from django.conf.urls import url
from django.contrib import admin
from loginpage.views import login, register

urlpatterns = [
    url(r'^register/$',register,name='register'),
    url(r'^login/$',login,name='login'),
    url(r'^admin/',admin.site.urls),
]
