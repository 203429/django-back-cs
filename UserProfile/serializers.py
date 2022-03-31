# Rest framework imports
from rest_framework import serializers

# Models imports
from UserProfile.models import user_profile_model

class user_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_profile_model
        fields = ('id_user','url_img')