# Generated by Django 2.0.2 on 2018-03-09 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0007_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='uniqid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
