# Generated by Django 3.2.9 on 2021-11-26 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0012_auto_20211122_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['id_paciente'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]
