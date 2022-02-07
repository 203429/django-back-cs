from django.urls import path, re_path
from django.conf.urls import include

# IMPORTACIONES
from loadImage.views import imageView
from loadImage.views import imagenViewDetail

urlpatterns = [
    re_path(r'^lista/$', imageView.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', imagenViewDetail.as_view()),
]