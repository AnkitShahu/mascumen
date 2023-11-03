from django.shortcuts import render
from .models import ProductDetails
# Create your views here.

def home(request): 
    context =  {'Products' : ProductDetails.objects.all()}
    print(context)
    return render(request, "home.html", context) 


def product(request, slug):
    try:
        product =  ProductDetails.objects.get(slug= slug)
        return render(request, 'product.html', context={'product': product})
    except Exception as e:
        print(e)

 