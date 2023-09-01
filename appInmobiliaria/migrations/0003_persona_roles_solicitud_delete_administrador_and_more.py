# Generated by Django 4.0.2 on 2022-05-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appInmobiliaria', '0002_inmueble'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=50)),
                ('telefonoPersona', models.IntegerField()),
                ('correoPersona', models.CharField(max_length=100)),
                ('estadoPersona', models.CharField(max_length=50)),
                ('solicitudPersona', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolNombre', models.CharField(max_length=50)),
                ('estadoRol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersona', models.CharField(max_length=50)),
                ('telefonoPersona', models.IntegerField()),
                ('correoPersona', models.CharField(max_length=100)),
                ('descripcionSolicitud', models.CharField(max_length=50)),
                ('estadoSolicitud', models.CharField(max_length=50)),
                ('fechaSolicitud', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.RenameField(
            model_name='inmueble',
            old_name='tipoNegocios',
            new_name='estadoInmueble',
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='descripcionInmueble',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='tituloInmueble',
            field=models.CharField(max_length=100),
        ),
    ]
