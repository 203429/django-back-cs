from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# IMPORTACIONES DE MODELOS AGREGADOS
from primerComponente.models import primer_tabla

# IMPORTACIONES DE SERIALIZADORES
from primerComponente.serializers import primer_tabla_serializer

# Create your views here.
class primer_tabla_list(APIView):
    def response_custom(self, message, data, status):
        response_json = {"message":message, "pay_load":data, "status":status}
        response_jsonb = json.dumps(response_json)
        final_response = json.loads(response_jsonb)
        return final_response

    def get(self, request, format = None):
        queryset = primer_tabla.objects.all()
        serializer=primer_tabla_serializer(queryset, many = True, context = {'request':request})
        return Response(self.response_custom("Success", serializer.data, status.HTTP_200_OK))

    def post(self, request, format = None):
        serializer = primer_tabla_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Success", datas, status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status.HTTP_400_BAD_REQUEST))

class primer_tabla_detail(APIView):
    def get_object(self, pk):
        try:
            return primer_tabla.objects.get(pk = pk)
        except primer_tabla.DoesNotExist:
            return 0
    
    def get(self, request, pk, format = None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = primer_tabla_serializer(id_response)
            return Response(id_response.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        id_response = self.get_object(pk)
        serializer = primer_tabla_serializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        objetive = self.get_object(pk)
        if objetive != "No existe":
            objetive.delete()
            return Response("Dato Eliminado", status = status.HTTP_200_OK)
        return Response("Dato no encontrado", status = status.HTTP_400_BAD_REQUEST)