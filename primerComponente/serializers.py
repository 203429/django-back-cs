from rest_framework import routers, serializers, viewsets

# IMPORTACIÓN DE MODELOS
from primerComponente.models import primer_tabla

class primer_tabla_serializer(serializers.ModelSerializer):
    class Meta:
        model = primer_tabla
        fields = ('__all__')