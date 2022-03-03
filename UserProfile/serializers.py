# Rest framework imports
from rest_framework import serializers

# Models imports
from UserProfile.models import userProfileModel

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfileModel
        fields = ('id_user','url_img')