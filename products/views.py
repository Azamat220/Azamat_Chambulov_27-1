from django.shortcuts import render, redirect
from products.models import Product, Review
from products.forms import ProductCreateForm, ReviewCreateForm


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products,
            'user': request.user
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
