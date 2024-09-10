from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Nama item ' : 'Oversize t-shirt kalcer',
        'Harga ': 'Rp198.000,00',
        'Deskripsi ': 'Baju lari untuk pelari kalcer Jakarta only'
    }

    return render(request, "main.html", context)