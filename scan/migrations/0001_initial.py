# Generated by Django 5.1 on 2024-08-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='processed_images/')),
                ('accuracy', models.FloatField(null=True)),
                ('object_counts', models.FloatField(null=True)),
            ],
        ),
    ]
