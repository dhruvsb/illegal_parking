# Generated by Django 2.0.2 on 2018-04-07 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0008_auto_20180407_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.CharField(max_length=10),
        ),
    ]
