# Generated by Django 5.1.4 on 2024-12-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario_creacion', models.IntegerField(blank=True, null=True)),
                ('id_creacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('id_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_estado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.CharField(blank=True, max_length=1, null=True)),
                ('usuario_creacion', models.IntegerField(blank=True, null=True)),
                ('id_creacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario_modificacion', models.IntegerField(blank=True, null=True)),
                ('id_modificacion', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_usuario',
                'managed': False,
            },
        ),
    ]
