from django.contrib.auth.hashers import make_password
from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)
    contrasena = models.CharField(max_length=64)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.contrasena:
            self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('AHORRO', 'ahorro'),
        ('CORRIENTE', 'corriente')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    numero = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_cuenta = models.CharField(max_length=100, choices=TIPO_CUENTA_CHOICES)

    def __str__(self):
        return f"Cuenta {self.numero} - Cliente: {self.cliente.nombre}"


class Movimiento(models.Model):
    TIPO_MOVIMIENTO_CHOICES = [
        ('DEPOSITO', 'Depósito'),
        ('RETIRO', 'Retiro')
    ]

    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='movimientos')
    tipo_movimiento = models.CharField(max_length=20, choices=TIPO_MOVIMIENTO_CHOICES)
    saldo_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_posterior = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.valor = abs(self.valor)
        self.saldo_anterior = self.cuenta.saldo
        if self.tipo_movimiento == 'RETIRO':
            self.saldo_posterior = self.saldo_anterior if self.saldo_anterior < self.valor\
                else self.saldo_anterior - self.valor
        elif self.tipo_movimiento == 'DEPOSITO':
            self.saldo_posterior = self.saldo_anterior + self.valor
        self.cuenta.saldo = self.saldo_posterior
        self.cuenta.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo_movimiento} - Cuenta: {self.cuenta.numero}"
