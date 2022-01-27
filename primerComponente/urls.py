from django.urls import path, re_path
from django.conf.urls import include

# IMPORTACIONES
from primerComponente.views import primerTablaList
from primerComponente.views import primerTablaDetail

urlpatterns = [
    re_path(r'^lista/$', primerTablaList.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', primerTablaDetail.as_view()),
]