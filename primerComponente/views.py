from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# IMPORTACIONES DE MODELOS AGREGADOS
from primerComponente.models import primerTabla

# IMPORTACIONES DE SERIALIZADORES
from primerComponente.serializers import primerTablaSerializer

# Create your views here.
class primerTablaList(APIView):
    def response_custom(self, message, data, status):
        responseJson = {"message":message, "pay_load":data, "status":status}
        responseJsonB = json.dumps(responseJson)
        finalResponse = json.loads(responseJsonB)
        return finalResponse

    def get(self, request, format = None):
        queryset = primerTabla.objects.all()
        serializer=primerTablaSerializer(queryset, many = True, context = {'request':request})
        return Response(self.response_custom("Success", serializer.data, status.HTTP_200_OK))
        # return Response(serializer.data)

    def post(self, request, format = None):
        serializer = primerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Success", datas, status.HTTP_201_CREATED))
            # return Response(datas, status = status.HTTP_201_CREATED)
        return Response(self.response_custom("Error", serializer.errors, status.HTTP_400_BAD_REQUEST))
        # return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class primerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return primerTabla.objects.get(pk = pk)
        except primerTabla.DoesNotExist:
            return 0
    
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = primerTablaSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        serializer = primerTablaSerializer(idResponse, data = request.data)
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