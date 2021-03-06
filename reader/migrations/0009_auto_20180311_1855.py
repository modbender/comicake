# Generated by Django 2.0.2 on 2018-03-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0008_auto_20180308_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='height',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='mime',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='page',
            name='size',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='width',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
