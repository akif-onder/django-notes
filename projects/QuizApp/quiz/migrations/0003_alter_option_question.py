# Generated by Django 4.1.1 on 2022-09-26 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_quiz_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='quiz.question'),
        ),
    ]
