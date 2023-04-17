from django.shortcuts import render
from products.models import Product

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def posts_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)

