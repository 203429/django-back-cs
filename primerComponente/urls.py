from django.urls import path, re_path
from django.conf.urls import include

from primerComponente.views import primerTablaList

urlpatterns = [
    re_path(r'^lista/$', primerTablaList.as_view()),    
]