from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Welcome to konohapedia',
        'price': 'harga terjangkau',
        'description': 'Semua produk yang dijual di tempat kami, 1000 persen ori',
        'rating': '5.0',
        'date': '7',

    }
    return render(request, "main.html", context)

def enter(request):
    if request.method == "POST":
        order = request.POST.get('order', '')  
        context = {
            'order': order,  
            'names': 'Welcome to konohapedia',
        }
    else:
        context = {
            'order': 'Tidak ada pesanan',
        }


    return render(request, "enter.html", context)


