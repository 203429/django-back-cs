from email.mime import image
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path, json

from loadImage.serializers import imageSerializer

from loadImage.models import imageModel

# Create your views here.
class imageView(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        responseOk = json.loads(res)
        return responseOk

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError("No has seleccionado la imagen para subir")
        archivo = request.data['url_img']
        nombre, formato = os.path.splitext(archivo.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = imageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.response_custom("Success",serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error",serializer.errors, status=status.HTTP_400_BAD_REQUEST))

    def get(self, request, format=None):
        queryset = imageModel.objects.all()
        serializer = imageSerializer(queryset , many=True, context={'request':request})
        return Response(self.response_custom("Success", serializer.data, status=status.HTTP_200_OK))

class imagenViewDetail(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        responseOk = json.loads(res)
        return responseOk

    def get_object(self, pk):
        try:
            return imageModel.objects.get(pk = pk)
        except imageModel.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = imageSerializer(id_response)
            return Response(self.response_custom("Success", id_response.data, status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", "No hay datos", status=status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.url_img.delete(save=True)
            id_response.delete()
            return Response(self.response_custom("Success", "Eliminado", status=status.HTTP_200_OK))
        return Response(self.response_custom("Error", "No se ha podido eliminar", status=status.HTTP_400_BAD_REQUEST))

    def put(self, request, pk, format = None):
        id_response = self.get_object(pk)
        archivo = request.data['url_img']
        nombre, formato = os.path.splitext(archivo.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = imageSerializer(id_response, data = request.data)
        if serializer.is_valid():
            id_response.url_img.delete(save=True)
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Success", datas, status = status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST))