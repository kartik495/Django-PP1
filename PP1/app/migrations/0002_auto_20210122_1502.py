# Generated by Django 3.1.5 on 2021-01-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task1',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
