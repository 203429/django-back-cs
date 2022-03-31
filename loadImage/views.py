from email.mime import image
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os.path, json

from loadImage.serializers import image_serializer

from loadImage.models import image_model

# Create your views here.
class image_view(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response_ok = json.loads(res)
        return response_ok

    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError("No has seleccionado la imagen para subir")
        archivo = request.data['url_img']
        nombre, formato = os.path.splitext(archivo.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = image_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.response_custom("Success",serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.response_custom("Error",serializer.errors, status=status.HTTP_400_BAD_REQUEST))

    def get(self, request, format=None):
        queryset = image_model.objects.all()
        serializer = image_serializer(queryset , many=True, context={'request':request})
        return Response(self.response_custom("Success", serializer.data, status=status.HTTP_200_OK))

class image_view_detail(APIView):
    def response_custom(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response_ok = json.loads(res)
        return response_ok

    def get_object(self, pk):
        try:
            return image_model.objects.get(pk = pk)
        except image_model.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = image_serializer(id_response)
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
        serializer = image_serializer(id_response, data = request.data)
        if serializer.is_valid():
            id_response.url_img.delete(save=True)
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Success", datas, status = status.HTTP_201_CREATED))
        return Response(self.response_custom("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST))