# Generated by Django 5.1 on 2024-10-21 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_userannouncementstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField()),
                ('remarks_at', models.DateTimeField(auto_now_add=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.submission')),
            ],
        ),
    ]
