# Generated by Django 2.0 on 2017-12-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0002_auto_20171219_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='celular',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='documento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
