# Generated by Django 3.1.1 on 2020-11-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_event_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.CharField(default='', max_length=25, verbose_name='Poster'),
        ),
    ]
