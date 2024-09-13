from django.urls import path
from  .views import (index ,books,view_all_books,delete_book,
                     add_new_book,Update,borrow_book,student_profile,view_book_details,update_student_profile, view_all_bookss)

urlpatterns = [
    path('', index, name='index'),
    path('books/',books , name='books'),
    path('all', view_all_books, name='books.all_books'),
    path('delete/<int:id>', delete_book, name='books.delete'),
    path('add_new_book', add_new_book, name='books.add_new_book'),
    path('books/<int:id>/update', Update, name='books.update'),
    path('spanel/all',view_all_bookss , name='indexs'),
    path('details/<int:id>', view_book_details, name='details'),
    path('borrow/', borrow_book, name='borrow_book'),
    path('profile/', student_profile, name='student_profile'),
    path('profile/update/', update_student_profile, name='update_student_profile'),
]