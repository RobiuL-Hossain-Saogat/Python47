# Generated by Django 5.0.6 on 2024-06-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(default=0, max_length=1083),
        ),
    ]