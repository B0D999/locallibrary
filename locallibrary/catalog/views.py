from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.views import generic


# Create your views here.


def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    return render(
        request,
        'index.html',
        context=
        {'num_books': num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


class BookListView(generic.ListView):
    model = Book

    def get(self, *args, **kwargs):
        context = {
            'books': Book.objects.all()
        }
        return render(self.request, 'catalog/book_list.html', context=context)



class BookDetailView(generic.DetailView):
    model = Book
