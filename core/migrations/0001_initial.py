# Generated by Django 4.2.3 on 2023-07-11 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=10, unique=True)),
                ('contrasena', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_cuenta', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuentas', to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_movimiento', models.CharField(choices=[('DEPOSITO', 'Depósito'), ('RETIRO', 'Retiro')], max_length=20)),
                ('saldo_anterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_posterior', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='core.cuenta')),
            ],
        ),
    ]
