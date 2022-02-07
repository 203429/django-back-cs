from rest_framework import routers, serializers, viewsets

from loadImage.models import imageModel

class imageSerializer(serializers.ModelSerializer):
    class Meta:
        model = imageModel
        fields = ('__all__')