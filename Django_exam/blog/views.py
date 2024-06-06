from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from blog.models import Product, Customers
from django.http import HttpResponseRedirect
from .forms import CustomerForm


# Create your views here.


def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/index.html', context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'blog/product-detail.html', context)

def customers(request):
    search_query = request.GET.get('filter', '')
    if search_query:
        customers = Customers.objects.filter(
        Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query)
        )
    else:
        customers = Customers.objects.all()

    # paginator = Paginator(customers, 4)
    # page_num = request.GET.get("page")
    # page = paginator.get_page(page_num)
        
    context = {
        'customers': customers,
        # 'page': page
    }
    return render(request, 'blog/customers.html', context)


def customer_detail(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    context = {
        'customer': customer
    }
    return render(request, 'blog/customer-detail.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = CustomerForm() 
    return render(request, 'blog/add_customer.html', {'form': form})



def edit_customer(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    if request.method == 'GET':
        return render(request, 'edit_customer.html', {'customer': customer})
    elif request.method == 'POST':
        image = request.FILES.get('image') 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        joined_at = request.POST.get('joined_at')
        
        customer.image = image
        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.phone = phone
        customer.address = address
        customer.joined_at = joined_at
        customer.save()
        
        return redirect('edit_customer', pk=pk)

 
    
def delete_customer(request, pk):
   
    return HttpResponseRedirect(reverse('customers'))
