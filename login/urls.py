from django.urls import path, re_path
from django.conf.urls import include

from login.views import loginAuth

urlpatterns = [
    re_path(r'^', loginAuth.as_view()),    
]