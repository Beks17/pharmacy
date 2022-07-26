from dataclasses import fields
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from multiprocessing import context
from os import name
from django.shortcuts import get_object_or_404, redirect, render
from requests import request
from .forms import *
from products.models import ActiveIngredient, MedClass, Product


# Create your views here.
def our_products_page(request):
    prd = Product.objects.all()
    context = {'products': prd}
    return render(request, 'main_page.html', context=context)


def search_product(request):
    search_text = request.GET.get('search-text')
    s_product = Product.objects.filter(name__icontains=search_text)
    context = {'search_products': s_product}
    return render(request, 'asd.html', context=context)

def add_product(request):
    print(request.POST)
    return render(request, 'add-product.html')

def med_class(request):
    mclass = MedClass.objects.all()
    ctx = {'mclass': mclass}
    return render(request, template_name='medclass.html', context=ctx)

def medclass_add(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return render(request, template_name='medclass_add.html')
        else:
            medclass = get_object_or_404(MedClass, pk=pk)
            ctx = {'medclass': medclass}
            return render(request, template_name='medclass_add.html', context=ctx)
    elif request.method == 'POST':
        if pk == 0:
            data = request.POST
            mclass = MedClass(
                name=data['name'])
            mclass.save()
        else:
            data = request.POST
            mclass = MedClass.objects.get(pk=data['pk'])
            mclass.name = data['name']
            mclass.save()
        return redirect('medclass')

def med_class_delete(request, pk):
    if request.method == 'GET':
        medclass = get_object_or_404(MedClass, pk=pk)
        ctx = {'medclass': medclass}
        return render(request, template_name='medclass_delete_conf.html', context=ctx)
    else:
        medclass = get_object_or_404(MedClass, pk=request.POST.get('pk'))
        medclass.delete()
        return redirect('medclass')

class ActiveIngredientListView(ListView):
    queryset = ActiveIngredient.objects.all()
    template_name = 'activeingredient.html'
    context_object_name = 'activeingredient'

class ActiveIngredientCreateView(CreateView):
    queryset = ActiveIngredient.objects.all()
    template_name = 'activeingredient_add.html'
    fields = "__all__"
    success_url = '/activeingredient'

class ActiveIngredientUpdateView(UpdateView):
    queryset = ActiveIngredient.objects.all()
    template_name = 'activeingredient_add.html'
    fields = "__all__"
    success_url = '/activeingredient'

class ActiveIngredientDeleteView(DeleteView):
    queryset = ActiveIngredient.objects.all()
    template_name = 'activeingredient_delete.html'
    fields = "__all__"
    success_url = '/activeingredient'

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'product.html'
    context_object_name = 'product'

    def get_queryset(self):
        url_data = self.request.GET
        q = Product.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        if 'activeingredient' in url_data and url_data['activeingredient']:
            q = q.filter(active_ingredient__name__icontains=url_data['activeingredient'])
        if 'price_from' in url_data and url_data['price_from']:
            q = q.filter(price_exw__gte=url_data['price_from'])
        if 'price_to' in url_data and url_data['price_to']:
            q = q.filter(price_exw__lte=url_data['price_to'])
        return q


class ProductCreateView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product_add.html'
    fields = '__all__'
    success_url = '/product'

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_add.html'
    fields = "__all__"
    success_url = '/product'

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    fields = "__all__"
    success_url = '/product'