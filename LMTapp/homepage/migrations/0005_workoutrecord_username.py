# Generated by Django 5.0.3 on 2024-03-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_workoutrecord_workout_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutrecord',
            name='username',
            field=models.CharField(default='user', max_length=150),
            preserve_default=False,
        ),
    ]