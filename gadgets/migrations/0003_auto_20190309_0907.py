# Generated by Django 2.0 on 2019-03-09 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0002_auto_20190125_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]