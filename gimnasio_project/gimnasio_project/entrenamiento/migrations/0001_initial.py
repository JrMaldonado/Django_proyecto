# Generated by Django 5.2.4 on 2025-07-14 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gimnasio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('numero_max_socios', models.IntegerField()),
                ('numero_contacto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlanEntrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion_semanas', models.IntegerField()),
                ('costo', models.DecimalField(decimal_places=2, max_digits=8)),
                ('gimnasio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrenamiento.gimnasio')),
            ],
        ),
    ]
