from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializer import *
from rest_framework.permissions import IsAuthenticated  
from rest_framework.views import APIView
from .models import *


class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]  # Bisa diakses tanpa login

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })

class ReservasiViewSet(viewsets.ModelViewSet):
    queryset = Reservasi.objects.all()
    serializer_class = ReservasiSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(id_admin=self.request.user)  

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        reservasi_aktif = Reservasi.objects.filter(id_admin=self.request.user, status="pending").first()
        if not reservasi_aktif:
            raise serializers.ValidationError({"detail": "Tidak ada reservasi aktif untuk transaksi ini."})

        serializer.save(reservasi=reservasi_aktif)  # Set otomatis ke reservasi yang ditemukan

class MejaViewSet(viewsets.ModelViewSet):
    queryset = Meja.objects.all()
    serializer_class = MejaSerializer
    permission_classes = [IsAuthenticated]

class MenuKategoriViewSet(viewsets.ModelViewSet):
    queryset = MenuKategori.objects.all()
    serializer_class = MenuKategoriSerializer
    permission_classes = [IsAuthenticated]

class StokViewSet(viewsets.ModelViewSet):  
    queryset = Stok.objects.all()
    serializer_class = StokSerializer
    permission_classes = [IsAuthenticated]

class TransaksiDetailViewSet(viewsets.ModelViewSet):
    queryset = TransaksiDetail.objects.all()
    serializer_class = TransaksiDetailSerializer
    permission_classes = [IsAuthenticated]

class ReservasiDetailViewSet(viewsets.ModelViewSet):
    queryset = Reservasi.objects.all()
    serializer_class = ReservasiDetailSerializer
    permission_classes = [IsAuthenticated]

