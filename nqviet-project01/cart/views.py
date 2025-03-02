from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from book.models import Book
from django.contrib.auth.decorators import login_required


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  # User đã đăng nhập
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required
def add_to_cart(request, book_id):
    # Lấy hoặc tạo giỏ hàng cho người dùng hiện tại
    cart, created = Cart.objects.get_or_create(user=request.user)
    book = get_object_or_404(Book, id=book_id)
    cart.books.add(book)  # Thêm sách vào giỏ
    return redirect('cart:cart_detail')  # Điều hướng về giỏ hàng


@login_required
def remove_from_cart(request, book_id):
    # Lấy giỏ hàng của người dùng hiện tại
    cart = get_object_or_404(Cart, user=request.user)
    book = get_object_or_404(Book, id=book_id)

    # Kiểm tra nếu sách có trong giỏ hàng
    if book in cart.books.all():
        cart.books.remove(book)

    return redirect('cart:cart_detail')


@login_required
def checkout(request):
    # Lấy giỏ hàng theo user đang đăng nhập
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.books.exists():
        return render(request, 'cart/checkout.html', {
            'cart': [],
            'total_price': 0
        })

    total_price = sum(book.price for book in cart.books.all())

    return render(request, 'cart/checkout.html', {
        'cart': cart.books.all(),
        'total_price': total_price
    })
