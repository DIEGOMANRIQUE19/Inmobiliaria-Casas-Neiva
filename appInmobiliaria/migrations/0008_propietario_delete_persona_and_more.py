# Generated by Django 4.2.3 on 2023-07-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appInmobiliaria', '0007_rename_barrioinmueble_inmueble_direccioninmueble_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePropietario', models.CharField(max_length=50)),
                ('telefonoPropietario', models.IntegerField()),
                ('correoPropietario', models.CharField(max_length=100)),
                ('fechaAgregacion', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='correoPersona',
            new_name='correoCliente',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='descripcionSolicitud',
            new_name='descripcionCliente',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='estadoSolicitud',
            new_name='estadoCliente',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='nombrePersona',
            new_name='nombreCliente',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='telefonoPersona',
            new_name='telefonoCliente',
        ),
    ]