# Generated by Django 5.1 on 2024-10-24 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_studentcomplaints_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcomplaints',
            name='complaint',
            field=models.TextField(),
        ),
    ]
