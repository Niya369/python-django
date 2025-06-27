from django.shortcuts import render , redirect
from .models import Order,OrderedItem
from products.models import Product
# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html', context)


# def add_to_cart(request):
#     if request.POST:
#         if not request.user.is_authenticated:
#           return redirect('login')  # or handle gracefully
#         user= request.user
#         customer= user.customer_profile
        

#         quantity=int(request.POST.get('quantity'))
#         product_id=request.POST.get('product_id')
#         product_obj = Product.objects.filter(pk=product_id).first()
#         if not product_obj:
#            return redirect('list_product')  # handle missing product
#         cart_obj,created=Order.objects.get_or_create(
#             owner=customer,
#             order_status=Order.CART_STAGE
#         )
#         product=product.objects.get(pk=product_id)
#         # product_obj = Product.objects.filter(pk=product_id).first()
        

        
#         ordered_item=OrderedItem.objects.create(
#             product=product,
#             owner=cart_obj,
#             quantity=quantity
#         )
        
#         return redirect('cart')


def add_to_cart(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # user must log in first

        user = request.user
        try:
            customer = user.customer_profile
        except AttributeError:
            # If customer profile missing, redirect to account page or show error
            return redirect('account')

        quantity = int(request.POST.get('quantity', 1))
        product_id = request.POST.get('product_id')
        product = Product.objects.filter(pk=product_id).first()
        if not product:
            return redirect('list_product')

        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        ordered_item, created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            defaults={'quantity': quantity}
        )
        if not created:
            ordered_item.quantity += quantity
            ordered_item.save()

        return redirect('cart')
