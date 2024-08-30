from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .model_facade import ModelFacade
from .models import ProcessedImage
from .serializer import ImageSerializer, ProcessedImageSerializer

# Create your views here.


class ScanViews(APIView):
    serializer_class = ImageSerializer

    def get(self, request, *args, **kwargs):
        return Response("Use Post Method to post images")

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data["image"]
            model = ModelFacade(image=image)
            model1 = ProcessedImage(accuracy=100)
            result = ProcessedImageSerializer(model1)
            return Response(result.data)
        return Response("Error uploading image")
