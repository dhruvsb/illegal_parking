# Generated by Django 2.0.2 on 2018-02-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0004_image_numbler_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.CharField(default='img1001', max_length=10),
        ),
    ]
