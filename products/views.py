from django.db.models import Q
from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm
from products.constants import PAGINATION_LIMIT

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)


        if search:
            products = products.filter(
                Q(title__icontains=search) |
                Q(composition__icontains=search))

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context)


def post_detial_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.review_set.all(),
            'form': ReviewCreateForm,
            'user': request.user
        }
        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = ReviewCreateForm(data=data)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )
            context = {
                'product': product,
                'review': product.review_set.all(),
                'form': form
            }

        return render(request, 'products/detail.html', context=context)


def post_create_view(request):
    if request.method == "GET":
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                composition=form.cleaned_data.get('composition'),
                rate=form.cleaned_data.get('rate')
            )

            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })
