import os

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from model.model import AcqaLens

from .serializer import UploadedImageSerializer


class ScanViews(APIView):
    serializer_class = UploadedImageSerializer

    def get(self, request, *args, **kwargs):
        return Response("Hello world")

    def post(self, request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            # image = serializer.validated_data["image"]
            # image_path = os.path.join(settings.MEDIA_ROOT, image.name)
            # with open(image_path, "wb+") as destination:
            #     for chunk in image.chunks():
            #         destination.write(chunk)
            # model = AcqaLens("best.pt")
            # model.predict(image_path)
            # results = model.properties()

            return Response({"Success here"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
