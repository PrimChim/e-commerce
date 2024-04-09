from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
# make admin login required to add product
@login_required(login_url='/admin/login/')
def add_product(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        price = data['price']
        description = data['description']
        image = request.FILES['image']
        product = Product(name=name, price=price, description=description, image=image)
        product.save()
        return render(request, 'products/add_product.html', {'message': 'Product added successfully'})
    return render(request, 'products/add_product.html')