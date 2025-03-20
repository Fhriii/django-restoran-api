from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Username atau password salah")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }
    
class ReservasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservasi
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class TransaksiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaksi
        fields = '__all__'

class MejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meja
        fields = '__all__'

class MenuKategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuKategori
        fields = '__all__'

class StokSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stok
        fields = '__all__'

class TransaksiDetailSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    class Meta:
        model = Transaksi
        fields = '__all__'

class ReservasiDetailSerializer(serializers.ModelSerializer):
    meja = MejaSerializer()
    class Meta:
        model = Reservasi
        fields = '__all__'

