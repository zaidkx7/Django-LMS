# Generated by Django 5.1 on 2024-10-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_quiz_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]
