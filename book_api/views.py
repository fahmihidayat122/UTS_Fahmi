from rest_framework import generics
from .models import Book
from .serializer import BookSerializer
from .models import Pembeli
from .serializer import PembeliSerializer
from .models import Pembelian
from .serializer import PembelianSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PembeliList(generics.ListCreateAPIView):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class PembelianList(generics.ListCreateAPIView):
    queryset = Pembelian.objects.all()
    serializer_class = PembelianSerializer


    