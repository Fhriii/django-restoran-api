from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login'),
router.register(r'reservasi',ReservasiViewSet,basename='reservasi')
router.register(r'menu',MenuViewSet,basename='menu')
router.register(r'transaksi',TransaksiViewSet,basename='transaksi')
router.register(r'meja',MejaViewSet,basename='meja')
router.register(r'menu_kategori',MenuKategoriViewSet,basename='menu_kategori')
router.register(r'stok',StokViewSet,basename='stok')
router.register(r'transaksi_detail',TransaksiDetailViewSet,basename='transaksi_detail')
 



urlpatterns = [
    path('', include(router.urls)),
    path('profile/', UserProfileView.as_view(), name='profile'),
]