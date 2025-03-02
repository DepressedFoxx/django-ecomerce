from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()  # Lấy toàn bộ danh sách customer
    return render(request, 'customer/customer_list.html', {'customers': customers})
