# Generated by Django 4.2.3 on 2023-07-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cuenta_tipo_cuenta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='numero',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]