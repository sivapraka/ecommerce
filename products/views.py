# Create your views here.
import logging

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Products, Orders, OrderProduct
from .serializer import ProductSerializer, CategorySerializer


def hello(request):
    return HttpResponse('Hello World')

def products(request):
    data=Products.objects.all()
    d=data[0]
    #print(data[0].name)
    d.name="New Name"
    d.save()
    print(data[0].name)
    products_list = serializers.serialize('json', data)
    #data = Products.objects.all()
    #products_list1 = json.dumps(list(data.values()), default=str)
    #combined_list = products_list + products_list1
    return JsonResponse(products_list, safe=False)
    # HTML Response
    #return HttpResponse(data.to_json())

@api_view(['GET'])
def products_list(request):
    data=Products.objects.all()
    products_list = ProductSerializer(data, many=True)
    return Response(products_list.data)

@api_view(['GET'])
def products_detail(request, id):
    try:
        data=Products.objects.get(id=id)
        products_list = ProductSerializer(data, many=False)
        return Response(products_list.data)
    except Products.DoesNotExist:
        return Response(status=404)

@api_view(['POST'])
def products_create(request):
    try:
        data=request.data
        serializer=ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=400)
    except KeyError:
        # Handle missing keys
        missing_keys = [key for key in ['name', 'price', 'description'] if key not in data]
        logging.error(f"Missing keys: {', '.join(missing_keys)}")
        return JsonResponse({'error': f'Missing keys: {", ".join(missing_keys)}'}, status=400)


@api_view(['POST'])
def category_create(request):
    try:
        data=request.data
        serializer=CategorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=200)
        else:
            return Response(data=serializer.errors, status=400)
    except KeyError:
        missing_keys = [key for key in ['name','description'] if key not in data]
        logging.error(f"Missing keys: {', '.join(missing_keys)}")
        return JsonResponse({'error': 'Missing keys: name'}, status=400)


@api_view(['GET'])
def products_category(request):
    data=Products.objects.select_related('category').all()
    products_list = ProductSerializer(data, many=True)
    return Response(products_list.data)


@api_view(['GET'])
def products_category_id(request, id):
    data=Products.objects.select_related('category').filter(category__id=id)
    products_list = ProductSerializer(data, many=True)
    return Response(products_list.data)

def test_error(request):
    raise ValueError("This is a test error!")


@api_view(['GET'])
def test(request):

    # Create products
    product1 = Products.objects.create(name="Product 1", price=100.00)
    product2 = Products.objects.create(name="Product 2", price=200.00)
    # Create an order
    order = Orders.objects.create(orderid="ORD123", order_status=True, total_price=0)
    # Add Products with Quantities
    OrderProduct.objects.create(order=order, product=product1, quantity=2)
    OrderProduct.objects.create(order=order, product=product2, quantity=3)
    # Calculate total price
    total_price = sum([op.product.price * op.quantity for op in OrderProduct.objects.filter(order=order)])
    order.total_price = total_price
    order.save()
    # Access products in the order
    print(order.product.all())
    # Access orders containing a product
    print(order)
    return HttpResponse("Test successful!")
