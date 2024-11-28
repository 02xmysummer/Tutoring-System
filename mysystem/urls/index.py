from django.urls import path, include
from mysystem.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("user/",include("mysystem.urls.user.index")),    
]
