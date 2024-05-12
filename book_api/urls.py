from django.urls import path
from .import views

urlpatterns = [
    path('book/', views.BookList.as_view(), name='book-list'),
    path('pembeli/', views.PembeliList.as_view(), name='pembeli-list'),
    path('pembelian/', views.PembelianList.as_view(), name='pembelian-list'),
]



