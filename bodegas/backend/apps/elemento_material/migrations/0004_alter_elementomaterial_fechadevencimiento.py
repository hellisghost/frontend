# Generated by Django 5.0.4 on 2024-09-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elemento_material', '0003_elementomaterial_sitio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementomaterial',
            name='FechaDevencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
