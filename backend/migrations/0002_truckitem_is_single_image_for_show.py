# Generated by Django 2.2.8 on 2021-04-04 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckitem',
            name='is_single_image_for_show',
            field=models.BooleanField(default=False),
        ),
    ]