# Generated by Django 3.0.7 on 2020-07-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0002_auto_20200709_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='work',
            field=models.TextField(blank=True),
        ),
    ]