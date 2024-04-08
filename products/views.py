from django.shortcuts import render

# Create your views here.
def add_product(request):
    return render(request, 'products/add_product.html')