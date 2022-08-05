# Generated by Django 3.2.5 on 2022-08-01 13:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toda',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='toda',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('99a2b2c2-ea46-4c6c-a882-64af71d7df3c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
