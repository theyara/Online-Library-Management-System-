from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Book
from .forms import BookForm


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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_role = request.POST['role']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user_role == 'admin':
                return redirect('admin_dashboard')
            elif user_role == 'student':
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def history_view(request):
    return render(request, 'history.html')

# Create your views here.
