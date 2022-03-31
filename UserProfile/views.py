# Django imports
from tkinter.messagebox import NO
from django.contrib.auth.models import User

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

# Others imports
import json

# Model imports
from UserProfile.models import user_profile_model

# Serializer imports
from UserProfile.serializers import user_profile_serializer

class user_profile_view(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def post(self, request):
        serializer = user_profile_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class user_profile_view_detail(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def custom_response_get(self, msg, user, data, status):
        data ={
            "message": msg,
            "first_name":user[0]['first_name'],
            "last_name":user[0]['last_name'],
            "username":user[0]['username'],
            "email":user[0]['email'],
            "id_user":user[0]['id'],
            "url_img":data.get('url_img'),
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get_object(self, pk):
        try:
            return user_profile_model.objects.get(id_user = pk)
        except user_profile_model.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        if user_profile != 0:
            user_profile = user_profile_serializer(user_profile)
            user = User.objects.filter(id=pk).values()
            return Response(self.custom_response_get("Success", user, user_profile.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "Profile not found", status=status.HTTP_400_BAD_REQUEST))

    def put(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        serializer = user_profile_serializer(user_profile, data=request.data)
        if serializer.is_valid():
            user_profile.url_img.delete(save=True)
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST))

    def delete(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        if user_profile != 0:
            user_profile.url_img.delete(save=True)
            return Response(self.custom_response("Success", "Deleted image", status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "Imgane not found", status=status.HTTP_400_BAD_REQUEST))

class user_profile_view_detail_data(APIView):
    def custom_response_get(self, msg, user, status):
        data ={
            "message": msg,
            "first_name":user[0]['first_name'],
            "last_name":user[0]['last_name'],
            "username":user[0]['username'],
            "email":user[0]['email'],
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def put(self, request, pk, format=None):
        user = User.objects.filter(id=pk)
        user.update(first_name = request.data.get('first_name'))
        user.update(last_name = request.data.get('last_name'))
        user.update(username = request.data.get('username'))
        user.update(email = request.data.get('email'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.custom_response_get("Actualizado", user2, status=status.HTTP_200_OK))