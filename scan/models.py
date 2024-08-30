from django.db import models

# Create your models here.


class ProcessedImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="processed_images/", null=True)
    accuracy = models.FloatField(null=True)
    object_counts = models.FloatField(null=True)
