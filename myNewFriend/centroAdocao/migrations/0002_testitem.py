# Generated by Django 3.0.8 on 2020-09-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centroAdocao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
