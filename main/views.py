from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'name': 'Welcome to konohapedia',
        'price': 'harga terjangkau',
        'description': 'Semua produk yang dijual di tempat kami, 1000 persen ori',
        'rating': '5.0',
        'date': '7',
        'product_entries': product_entries,

    }
    return render(request, "main.html", context)

# def enter(request):
#     if request.method == "POST":
#         order = request.POST.get('order', '')  
#         context = {
#             'order': order,  
#             'names': 'Welcome to konohapedia',
#         }
#     else:
#         context = {
#             'order': 'Tidak ada pesanan',
#         }


#     return render(request, "enter.html", context)


def enter(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "enter.html", context)


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


