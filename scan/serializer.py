from rest_framework import serializers
from .models import ProcessedImage
class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

class ProcessedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedImage
        fields = '__all__'