# Generated by Django 2.0.2 on 2018-03-27 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0027_auto_20180326_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='published_at',
        ),
    ]
