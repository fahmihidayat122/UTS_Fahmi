from rest_framework import serializers
from .models import Book
from .models import Pembeli
from .models import Pembelian

class BookSerializer(serializers.ModelSerializer):
    buku = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='buku-detail'
    )
    class Meta:
        model = Book
        fields = ["id", "judul", "penulis", "harga", 'buku']

class PembeliSerializer(serializers.ModelSerializer):
    pembelian_pembeli = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='pembelian-detail'
    )
    class Meta:
        model = Pembeli
        fields = ["id", "nama", "alamat", "email", 'pembelian_pembeli']

class PembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembelian
        fields = ["id", "book", "pembeli", "jumlah", "tanggal_beli"]
