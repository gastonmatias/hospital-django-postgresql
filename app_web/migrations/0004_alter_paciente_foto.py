# Generated by Django 3.2.8 on 2021-10-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_web', '0003_auto_20211028_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(blank='True', default='/media/fotos/profile_default.jpg', null=True, upload_to='fotos', verbose_name='Fotografia (Opcional)'),
        ),
    ]
