from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import ProductSerializer, StockSerializer
from base.models import Product, Stock

def createProduct(request):
  data = request.data

  serializer = ProductSerializer(data=data)
  if(serializer.is_valid()):
    product_instance = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getProducts(request):
  products = get_list_or_404(Product.objects.all())
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

def getProduct(request, pk):
  product = get_object_or_404(Product, pk=pk)
  serializer = ProductSerializer(product, many=False)
  return Response(serializer.data, status=status.HTTP_200_OK)

def deleteProduct(request, pk):
  product = get_object_or_404(Product, pk=pk)
  product.delete()
  return Response("Product was deleted!", status=status.HTTP_200_OK)

def updateProduct(request, pk):
  data = request.data
  product = get_object_or_404(Product, pk=pk)
  serializer = ProductSerializer(product, data=data)

  if(serializer.is_valid()):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# For now we'll have two ways of adding stock. Either bulk, or manually.
# For bulk, data should look something like this:
  # [
  #   {
  #     "product": 1
  #     "quantity": 30
  #   },
  #   ...
  # ]
# And we'll make 30 entries on the table. Horrible, but better for the user if they have to add a bunch of stock and we don't have a better way implemented yet, like with a barcode scanner (which would be ideal).
# For manual, data will only be the product_id of the product we're stocking.
# DBulacio 31/12/23
def addBulkStock(request):
  try:
    data = request.data
    for entry in data:
      product_id = entry.get("product")
      product = Product.objects.get(pk=product_id)

      Stock.objects.create(product=product) # date_in should be set
    return Response("Stock successfully added", status=status.HTTP_200_OK)
  except Exception as e:
    return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

def addManualStock(request):
  data = request.data # should only be {"product":x}

  serializer = StockSerializer(data=data)
  if(serializer.is_valid()):
    stock_instance = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# getStockByProduct -> int
def getStockByProduct(request, pk):
  stock = Stock.objects.filter(product=pk, date_out__isnull=True).count()
  serializer = StockSerializer(stock, many=True)
  return Response(serializer.data, status=status.HTTP_201_CREATED)

# takeStock -> updatea el stock más viejo que tengamos del producto siempre y cuando exista alguno.
