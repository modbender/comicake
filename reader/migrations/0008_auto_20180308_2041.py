# Generated by Django 2.0.2 on 2018-03-09 04:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0007_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chapter',
            name='uniqid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
