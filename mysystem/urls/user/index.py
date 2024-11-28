from django.urls import path
from mysystem.utils.Authentication import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from mysystem.views.user.userlist import UserList
from mysystem.views.user.register import Register
from mysystem.views.user.userinfo import UserInfo


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("userlist/",UserList.as_view(),name="mysystem_user_userList"),
    path("register/",Register.as_view(),name="mysystem_user_register"),
    path("userinfo/",UserInfo.as_view(),name="mysystem_user_userinfo"),
]
