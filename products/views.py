from django.shortcuts import render
from .models import Product
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request,'index.html')


# def index(request):
#     product_list = Product.objects.all()
#     context = {'products': product_list}
#     return render(request, 'index.html', context)

def list_product(request):
    """_summary_
    returns product list page
    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    product_list = Product.objects.all()
    # product_paginator = Paginator(product_list,2)
    # product_list = product_paginator.get_page(1)
    # context= {'products': page}
    # page_obj = Paginator.get_page(1)
    # context = {'products': page_obj}
    context= {'products':product_list}
    return render(request,'products.html',context)

# def detail_product(request, pk):
#     if request.POST:
#         print(request.POST)
#     return render(request,'product_detail.html')

def detail_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404("Product not found")

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'product_detail.html', {'product': product})

# def detail_product(request, pk):
#     Product=Product.objects.get(pk=pk)
#     context={'product':Product}
#     return render(request, 'product_detail.html', context)










# from django.shortcuts import render
# from .models import Product
# from django.core.paginator import Paginator

# def index(request):
#      return render(request,'index.html')

# def list_product(request):
#     """Returns product list page with pagination."""
#     product_list = Product.objects.all()
#     paginator = Paginator(product_list, 2)  # Show 2 products per page

#     page_number = request.GET.get('page')  # Get the current page number
#     page_obj = paginator.get_page(page_number)  # Get the page object

#     context = {'products': page_obj}
#     return render(request, 'products.html', context)


# def detail_product(request):
#     return render(request,'product_detail.html')
