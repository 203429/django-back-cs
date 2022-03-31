from django.urls import path, re_path
from django.conf.urls import include

# IMPORTACIONES
from primerComponente.views import primer_tabla_list
from primerComponente.views import primer_tabla_detail

urlpatterns = [
    re_path(r'^lista/$', primer_tabla_list.as_view()),
    re_path(r'^lista/(?P<pk>\d+)$', primer_tabla_detail.as_view()),
]