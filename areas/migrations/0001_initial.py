# Generated by Django 2.0.2 on 2018-02-15 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('area_id', models.IntegerField(default=100)),
                ('operator', models.CharField(max_length=255)),
                ('order_id', models.IntegerField(default=1)),
                ('pincode', models.IntegerField(default=395001)),
            ],
        ),
    ]