<<<<<<< HEAD
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


    
=======
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all() #Complex Data
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
>>>>>>> ae0b8d3a0db8bf0bfdf5a3847d438cf155e0ffe6
