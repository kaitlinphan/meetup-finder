# Generated by Django 3.1.1 on 2020-11-09 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('location', models.CharField(max_length=150, verbose_name='Location')),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('xcoord', models.FloatField(default=0.0)),
                ('ycoord', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.event')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
