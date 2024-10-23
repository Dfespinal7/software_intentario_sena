# Generated by Django 5.1.2 on 2024-10-22 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_salidas_totalvalorsal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('rol', models.IntegerField(choices=[(1, 'administrador'), (2, 'empleado')], default=2)),
            ],
        ),
    ]