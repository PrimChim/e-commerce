from django.shortcuts import render
from products.models import Product, ProductLike
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
@login_required
def home(request):
    
    products = Product.objects.all()

    # add a new key likes to each product
    for product in products:
        product.likes = ProductLike.objects.filter(product=product).count()

    # sort products by likes
    products = sorted(products, key=lambda x: x.likes, reverse=True)

    context = {
        'products': products
    }

    if request.method == 'POST':
        user = request.user
        data = request.POST
        product_id = data['product_id']
        product = Product.objects.get(id=product_id)

        already_liked = ProductLike.objects.filter(product=product, user=user).exists()
        if not already_liked:
            like = ProductLike.objects.create(product=product, user=user)
            like.save()
        else:
            ProductLike.objects.filter(product=product, user=user).delete()


    return render(request, 'users/index.html', context)

def login_view(request):
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        password = data['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})

    return render(request, 'users/login.html')