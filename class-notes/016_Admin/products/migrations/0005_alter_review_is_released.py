# Generated by Django 4.1.1 on 2022-09-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='is_released',
            field=models.BooleanField(default=False),
        ),
    ]
