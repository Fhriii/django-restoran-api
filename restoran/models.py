# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'admin'


class Meja(models.Model):
    id_meja = models.AutoField(primary_key=True)
    no_meja = models.CharField(unique=True, max_length=100)
    kapasitas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'meja'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nama_menu = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    id_kategori = models.ForeignKey('MenuKategori', models.DO_NOTHING, db_column='id_kategori')

    class Meta:
        managed = False
        db_table = 'menu'


class MenuKategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'menu_kategori'


class Reservasi(models.Model):
    id_reservasi = models.AutoField(primary_key=True)
    id_meja = models.ForeignKey(Meja, models.DO_NOTHING, db_column='id_meja', blank=True, null=True)
    id_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='id_admin', blank=True, null=True)
    nama_customer = models.CharField(max_length=100)
    tanggal_reservasi = models.DateTimeField()
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'reservasi'


class Stok(models.Model):
    id_stok = models.AutoField(primary_key=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu', blank=True, null=True)
    jumlah_stok = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stok'


class Transaksi(models.Model):
    id_transaksi = models.AutoField(primary_key=True)
    id_reservasi = models.ForeignKey(Reservasi, models.DO_NOTHING, db_column='id_reservasi', blank=True, null=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    ppn = models.DecimalField(max_digits=10, decimal_places=0)
    diskon = models.DecimalField(max_digits=10, decimal_places=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status_pembayaran = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaksi'


class TransaksiDetail(models.Model):
    id_detail = models.AutoField(primary_key=True)
    id_transaksi = models.ForeignKey(Transaksi, models.DO_NOTHING, db_column='id_transaksi', blank=True, null=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu', blank=True, null=True)
    jumlah = models.IntegerField(blank=True, null=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaksi_detail'
