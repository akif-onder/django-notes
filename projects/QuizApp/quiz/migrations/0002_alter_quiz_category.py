# Generated by Django 4.1.1 on 2022-09-26 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quiz",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quizz",
                to="quiz.category",
            ),
        ),
    ]
