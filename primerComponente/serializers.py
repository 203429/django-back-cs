from dataclasses import field
from rest_framework import routers, serializers, viewsets

# IMPORTACIÓN DE MODELOS
from primerComponente.models import primerTabla

class primerTablaSerializer(serializers.ModelSerializer):
    class meta:
        model = primerTabla
        fields = ('nombre','edad')