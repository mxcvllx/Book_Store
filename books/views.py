from django.views import ListView

from books.models import Book


class HomeView(ListView):
    query_set = Book.objects.order_by("-id")
    template_name = 'home.html'
