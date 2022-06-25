from multiprocessing import context
from django.shortcuts import render
from requests import request

from products.models import Product


# Create your views here.
def our_products_page(request):

    prd = Product.objects.all()
    context = {'products': prd}

    return render(request, 'main_page.html', context=context)


