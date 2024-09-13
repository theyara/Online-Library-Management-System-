from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRecord,S
from .forms import BookForm
from django.http import HttpResponseNotFound
from .forms import StudentProfileForm, BorrowBookForm


def view_all_bookss(request):
    books = Book.objects.all()
    return render(request, "indexs.html", {"books": books})


def view_book_details(request, id):
    book_details = get_object_or_404(Book, id=id)
    return render(request, "details.html", {"book": book_details})


def borrow_book(request):
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book'].name
            try:
                # Ensure the book exists
                book = Book.objects.get(name=book_name)
            except Book.DoesNotExist:
                form.add_error(None, 'The selected book does not exist.')
                return render(request, 'borrow.html', {'form': form})

            try:
                # Ensure the student record exists for the current user
                student = S.objects.get(user=request.user)
            except S.DoesNotExist:
                form.add_error(None, 'Student record not found.')
                return render(request, 'borrow.html', {'form': form})

            if book.available:
                # Create the BorrowRecord entry
                BorrowRecord.objects.create(student=student, book=book)
                book.available = False
                book.save()
                url = reverse('indexs')
                return redirect(url)  # Redirect to a success page or message
            else:
                form.add_error(None, 'This book is not available for borrowing.')

    else:
        form = BorrowBookForm()

    return render(request, 'borrow.html', {'form': form})


@login_required
def student_profile(request):
    try:
        student = S.objects.get(user=request.user)
    except S.DoesNotExist:
        return HttpResponseNotFound('Student profile does not exist.')

    borrow_records = BorrowRecord.objects.filter(student=student)

    return render(request, 'student_profile.html', {
        'student': student,
        'borrow_records': borrow_records
    })


@login_required
def update_student_profile(request):
    student = S.objects.get(user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=student)

    return render(request, 'update_student_profile.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def books(request):
    books = [
        {"name": "How Innovation Works", "auther": " Matt Ridley ",
         "description": "Innovation is an evolutionary process. The starting ingredients are freedom and a basic level of prosperity within society",
         "image": "img1 (2).jpg"},
        {"name": "The phsycology of Money", "auther": " Morgan Housel ",
         "description": "Overall: The Psychology of Money is a refreshing and insightful book that offers a unique perspective on the relationship between money and human behavior.",
         "image": "img2 (2).jpg"},
        {"name": "Hooked", "auther": " Nir Eyal ",
         "description": "This book offers invaluable insights into the psychology behind creating products that captivate and retain users. Highly recommended for anyone involved in product development.",
         "image": "img3 (3).jpg"},
        {"name": "Seeds Planted in Concrete", "auther": " Bianca Sparacino ",
         "description": "This collection is a manifesto of the journey every human being takes throughout their life; an assembly of words that celebrates the resilience of the human heart through stages of hurting, feeling, healing and loving. Bianca Sparacino?s first collection of work is one that will speak to the very depths of those who read it, inspiring a will to love, and live.",
         "image": "img4 (3).jpg"},
    ]
    return render(request, 'books.html', {'books': books})


def view_all_books(request):
    books = Book.objects.all()
    return render(request, "books/all_books.html", {"books": books})


def delete_book(request, id):
    deleted_book = get_object_or_404(Book, id=id)
    deleted_book.delete()
    url = reverse("books.all_books")
    return redirect(url)


def Update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            url = reverse('books.all_books')
            return redirect(url)

    return render(request, 'books/update.html', {'form': form})


def add_new_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            new_book = Book()
            new_book.name = request.POST["name"]
            new_book.author = request.POST["author"]
            new_book.published_date = request.POST["published_date"]
            new_book.image = request.FILES["image"]
            new_book.save()
            url = reverse("books.all_books")
            return redirect(url)
    return render(request, 'books/add_new_book.html', {"form": form})





# Create your views here.
