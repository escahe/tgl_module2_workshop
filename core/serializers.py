from rest_framework import serializers
from .models import Cliente, Cuenta, Movimiento

class MovimientoSerializer(serializers.ModelSerializer):
    saldo_anterior = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    saldo_posterior = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = Movimiento
        fields = '__all__'


class CuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuenta
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'
