from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# IMPORTACIONES DE MODELOS AGREGADOS
from primerComponente.models import primerTabla

# IMPORTACIONES DE SERIALIZADORES
from primerComponente.serializers import primerTablaSerializer

# Create your views here.
class primerTablaList(APIView):
    def get(self, request, format=None):
        queryset=primerTabla.objects.all()
        serializer=primerTablaSerializer(queryset,many=True ,context={'request':request})
        return Response(serializer.data)