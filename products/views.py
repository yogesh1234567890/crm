from django.shortcuts import render, redirect,get_object_or_404
from .models import Products
from .forms import ProductsForm


# Create your views here.
def ProductView(request):
    data = Products.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'html/basic-table.html', context=context)


def create_products(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form = ProductsForm()
    return render(request, 'html/forms.html', {
        'form': form
    })


def update_products(request, id):
    product_object=instance=get_object_or_404(Products,id=id)
    if request.method == "POST":
        form = ProductsForm(request.POST,instance=product_object)
        if form.is_valid():
            form.save()
            return redirect('/products')
        else:
            print("Form is invalid")
    else:
        form = ProductsForm(instance=product_object)
    return render(request, 'html/update.html', {
        'form': form
    })

def delete_products(request,id):
    product_object = instance = get_object_or_404(Products, id=id)
    product_object.delete()
    return redirect('/products')
