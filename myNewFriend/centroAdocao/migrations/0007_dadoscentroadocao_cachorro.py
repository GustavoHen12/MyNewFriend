# Generated by Django 3.0.8 on 2020-09-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroAdocao', '0006_dadoscentroadocao_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadoscentroadocao',
            name='cachorro',
            field=models.BooleanField(default=False),
        ),
    ]