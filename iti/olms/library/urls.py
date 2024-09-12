from django.urls import path
from  .views import (index , register_view , logout_view , login_view ,
                     history_view , profile_view, books,view_all_books,delete_book,add_new_book,Update)

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('history/', history_view, name='history'),
    path('books/',books , name='books'),
    path('all', view_all_books, name='books.all_books'),
    path('delete/<int:id>', delete_book, name='books.delete'),
    path('add_new_book', add_new_book, name='books.add_new_book'),
    path('books/<int:id>/update', Update, name='books.update'),
]