# Generated by Django 5.0.4 on 2024-04-18 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0002_remove_area_programa_area'),
        ('sede', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('area_AreaSede', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='area.area')),
                ('persona_administra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sede_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sede.sede')),
            ],
        ),
    ]
