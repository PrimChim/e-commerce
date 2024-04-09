from django.shortcuts import render
from products.models import Product, ProductLike
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.
def home(request):
    
    products = Product.objects.all()

    search_product = request.GET.get('search')
    if search_product != "" and search_product is not None:
        products = Product.objects.filter(name__icontains=search_product)


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

    # add a new key likes to each product
    for product in products:
        product.likes = ProductLike.objects.filter(product=product).count()

    # sorting products in descending order of likes
    products = sorted(products, key=lambda x: x.likes, reverse=True)
    context = {
        'products': products
    }
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