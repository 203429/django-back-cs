from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# importaciones de modelos agregados
from primerComponente.models import primerTabla

# importaciones de serializadores
from primerComponente.serializers import primerTablaSerializer

# Create your views here.
class primerTablaList(APIView):
    def get(self, request, format=None):
        queryset=primerTabla.objects.all()
        serializer=primerTablaSerializer(queryset,many=True ,context={'request':request})
        return Response(serializer.data)