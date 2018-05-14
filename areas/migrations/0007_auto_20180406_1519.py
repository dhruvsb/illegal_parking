# Generated by Django 2.0.2 on 2018-04-06 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0006_auto_20180215_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='area_id',
            field=models.IntegerField(default=100, unique=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='areas.Area'),
        ),
        migrations.AlterField(
            model_name='image',
            name='number_plate',
            field=models.CharField(default='GJ-05-0000', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('image_id', 'area')},
        ),
    ]