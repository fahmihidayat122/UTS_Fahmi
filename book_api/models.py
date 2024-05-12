from django.db import models
<<<<<<< HEAD
from django.core.validators import MaxLengthValidator

# Create your models here.
class Book(models.Model):
    judul = models.CharField(max_length=100, default='Judul Default')
    penulis = models.CharField(max_length=100, default='Penulis Default')
    harga = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def str(self):
        return self.judul
    
class Pembeli(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.nama
    
class Pembelian(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='buku')
    pembeli = models.ForeignKey(Pembeli, on_delete=models.CASCADE,related_name='pembelian_pembeli')
    jumlah = models.PositiveIntegerField()
    tanggal_beli = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.book
=======

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
    



#   /books/list
>>>>>>> ae0b8d3a0db8bf0bfdf5a3847d438cf155e0ffe6
