# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Others imports
import json

# Model imports
from UserProfile.models import userProfileModel

# Serializer imports
from UserProfile.serializers import userProfileSerializer

class userProfileView(APIView):
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
        serializer = userProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_201_CREATED))
        return Response(self.custom_response("Error", serializer.errors, status=status.HTTP_400_BAD_REQUEST))

class userProfileViewDetail(APIView):
    def custom_response(self, msg, response, status):
        data ={
            "messages": msg,
            "pay_load": response,
            "status": status,
        }
        res= json.dumps(data)
        response = json.loads(res)
        return response

    def get_object(self, pk):
        try:
            return userProfileModel.objects.get(id_user = pk)
        except userProfileModel.DoesNotExist:
            return 0

    def get(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        if userProfile != 0:
            userProfile = userProfileSerializer(userProfile)
            return Response(self.custom_response("Success", userProfile.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "Profile not found", status=status.HTTP_400_BAD_REQUEST))

    def put(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = userProfileSerializer(userProfile, data=request.data)
        if serializer.is_valid():
            userProfile.url_img.delete(save=True)
            serializer.save()
            return Response(self.custom_response("Success", serializer.data, status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", serializer.errors, status = status.HTTP_400_BAD_REQUEST))
            

    def delete(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        if userProfile != 0:
            userProfile.url_img.delete(save=True)
            return Response(self.custom_response("Success", "Deleted image", status=status.HTTP_200_OK))
        return Response(self.custom_response("Error", "Imgane not found", status=status.HTTP_400_BAD_REQUEST))