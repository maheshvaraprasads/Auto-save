# Generated by Django 2.2.13 on 2021-06-30 10:49

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
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zignum', models.CharField(max_length=255, null=True, verbose_name='Scan Zig_Number')),
                ('unitsn', models.CharField(max_length=255, null=True, verbose_name='Scan Unit Sn')),
                ('crew', models.CharField(max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Data',
                'verbose_name_plural': 'Datas',
                'ordering': ['-created'],
            },
        ),
    ]