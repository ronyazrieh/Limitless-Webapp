# Generated by Django 5.0.1 on 2024-04-12 00:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_workoutrecord_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('target_sets', models.IntegerField(default=0)),
                ('completed_sets', models.IntegerField(default=0)),
                ('target_workouts', models.IntegerField(default=0)),
                ('completed_workouts', models.IntegerField(default=0)),
                ('goal_completed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
