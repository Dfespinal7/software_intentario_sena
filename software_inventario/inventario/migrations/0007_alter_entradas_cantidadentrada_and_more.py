# Generated by Django 5.0.6 on 2024-08-28 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0006_alter_salidas_valorunidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='cantidadEntrada',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='observacion',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='unidadMedida',
            field=models.CharField(default=0, max_length=150),
        ),
        migrations.AlterField(
            model_name='entradas',
            name='valorUnidad',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='productos',
            name='unidadMedida',
            field=models.CharField(default='sin unidad de medida', max_length=150),
        ),
        migrations.AlterField(
            model_name='salidas',
            name='cantidadSalida',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='salidas',
            name='observacion',
            field=models.CharField(default='sin Observacion', max_length=150),
        ),
        migrations.AlterField(
            model_name='salidas',
            name='valorUnidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockinventarios',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockinventarios',
            name='valorInvenario',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockinventarios',
            name='valorUnidad',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=30),
        ),
    ]
