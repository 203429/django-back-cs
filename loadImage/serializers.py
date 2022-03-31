from rest_framework import routers, serializers, viewsets

from loadImage.models import image_model

class image_serializer(serializers.ModelSerializer):
    class Meta:
        model = image_model
        fields = ('__all__')