from django.urls import path
from .views import *


urlpatterns = [
    path('login/', UsersLoginView.as_view(), name="login")
]
