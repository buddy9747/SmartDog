# Generated by Django 2.0 on 2019-01-25 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catlog',
            name='category',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
