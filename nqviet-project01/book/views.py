from django.shortcuts import render, get_object_or_404
from .models import Book
from cart.models import Cart
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import SignUpForm
from .forms import BookForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect("book_list")  # Chuyển hướng sau khi đăng ký thành công
    else:
        form = SignUpForm()
    return render(request, "registrations/signup.html", {"form": form})


def book_list(request):
    books = Book.objects.all()

    # Lấy từ khóa tìm kiếm từ request
    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(title__icontains=search_query)  # Tìm theo tên sách

    # Lọc theo giá
    price_filter = request.GET.get('price', '')
    if price_filter:
        if price_filter == 'low':
            books = books.order_by('price')  # Giá thấp đến cao
        elif price_filter == 'high':
            books = books.order_by('-price')  # Giá cao đến thấp

    return render(request, 'book/book_list.html',
                  {'books': books, 'search_query': search_query, 'price_filter': price_filter})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(id=1)
    return render(request, 'book/cart_detail.html', {'cart': cart})


def logout_view(request):
    return render(request, 'registrations/logout.html')


def login_view(request):
    return render(request, 'registrations/login.html')


def signup_view(request):
    return render(request, 'registrations/signup.html')


# Thêm sách mới
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})


# Cập nhật sách
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})


# Xóa sách
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})