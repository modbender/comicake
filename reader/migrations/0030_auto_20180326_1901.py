# Generated by Django 2.0.2 on 2018-03-27 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0029_auto_20180326_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='volume',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
