from django.urls import path
from loginSystem import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    
#     path('login/', views.Login.as_view(), name='login'),
#     path('register/', views.Register.as_view(), name='login'),
  
#     path('api/token/', obtain_jwt_token),
#     path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
]
from rest_framework_jwt.views import obtain_jwt_token
#...

urlpatterns = [
    # ...

    path('api-token-auth/', obtain_jwt_token),
]

