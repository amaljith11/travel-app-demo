# Generated by Django 5.0.4 on 2024-04-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(null=True, upload_to='hari'),
        ),
    ]
