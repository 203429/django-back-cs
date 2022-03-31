from django.urls import path, re_path
from django.conf.urls import include

# IMPORTACIONES
from loadImage.views import image_view
from loadImage.views import image_view_detail

urlpatterns = [
    re_path(r'^lista/$', image_view.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', image_view_detail.as_view()),
]