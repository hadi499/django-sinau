from django.shortcuts import render, get_object_or_404
from .models import Book, Page

def book_list(request):
    # Mengambil semua Book dari database
    books = Book.objects.all()
    return render(request, 'book/list.html', {'books': books})

def book_detail(request, book_id):
  
    book = get_object_or_404(Book, id=book_id)   
  
    pages = book.page_set.all() 
    
    return render(request, 'book/page.html', {'book': book, 'pages': pages})


def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)  
    return render(request, 'book/detail.html', {'page': page})