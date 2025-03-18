# Generated by Django 5.1.6 on 2025-03-06 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0004_planestudio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('PlanEstudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.planestudio')),
            ],
        ),
    ]
