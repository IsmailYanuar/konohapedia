from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306245781',
        'name': 'Welcome to konohapedia',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
