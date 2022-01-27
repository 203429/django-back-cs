from rest_framework import routers, serializers, viewsets

# IMPORTACIÓN DE MODELOS
from primerComponente.models import primerTabla

class primerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = primerTabla
        fields = ('__all__')