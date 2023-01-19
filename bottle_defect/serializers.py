from rest_framework import serializers
from .models import upload_image

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        print("models.py")
        model = upload_image
        #fields = ["images"]
        fields = "__all__"