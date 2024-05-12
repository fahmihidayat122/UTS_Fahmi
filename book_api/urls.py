<<<<<<< HEAD
from django.urls import path
from .import views

urlpatterns = [
    path('book/', views.BookList.as_view(), name='book-list'),
    path('pembeli/', views.PembeliList.as_view(), name='pembeli-list'),
    path('pembelian/', views.PembelianList.as_view(), name='pembelian-list'),
]



=======

from django.contrib import admin
from django.urls import path
from book_api.views import  book_list, book_create

urlpatterns = [
    path('', book_create),
    path('list/', book_list)
]


>>>>>>> ae0b8d3a0db8bf0bfdf5a3847d438cf155e0ffe6
