from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.


def test_api_view(request):
    first_product = Product.objects.first()
    # s = json.dumps(first_product)
    f_b = {
        'name': first_product.name,
        'reg_num': first_product.reg_num,
        'med_isntruction': first_product.med_isntruction,
        'release_form': first_product.release_form,
        'min_order': first_product.min_order,
        'price_exw': first_product.price_exw,
        'med_image': str(first_product.med_image),
        'active_ingredient': [item.name for item in first_product.active_ingredient.all()],
        'med_class': first_product.med_class.name,
    }
    return JsonResponse(f_b)


@api_view(['GET', 'POST'])
def product_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ProductSerializer(instance=Product.objects.all(), many=True).data, status=200)
        else:
            the_product = get_object_or_404(Product, pk=pk)
            return Response(data=ProductSerializer(instance=the_product).data, status=200)
    elif request.method == 'POST':
        sb = ProductSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)

