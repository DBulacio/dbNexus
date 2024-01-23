from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import ProductSerializer, StockSerializer
from base.models import Product, Stock
from django.db.models import Min
from django.utils import timezone

def createProduct(request):
  data = request.data

  serializer = ProductSerializer(data=data)
  if(serializer.is_valid()):
    product_instance = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def getProducts(request):
  products = get_list_or_404(Product.objects.filter(is_active=True))
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

    # Check if all products exist
    non_existing_product_ids = [entry.get("product") for entry in data if not Product.objects.filter(pk=entry.get("product")).exists()]
    if non_existing_product_ids:
      return Response("Trying to add non existing products", status=status.HTTP_400_BAD_REQUEST)

    for entry in data:
      product_id = entry.get("product")
      product = Product.objects.get(pk=product_id)

      for i in range(entry.get("quantity")):
        Stock.objects.create(product=product) # date_in should be set

    return Response(data, status=status.HTTP_200_OK)
  except Exception as e:
    return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

def addManualStock(request):
  data = request.data # should only be {"product":x}

  serializer = StockSerializer(data=data)
  if(serializer.is_valid()):
    stock_instance = serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# getStockByProduct -> returns stock amount
def getStockByProduct(request, product_id):
  stock = Stock.objects.filter(product=pk, date_out__isnull=True).count()
  return Response(stock, status=status.HTTP_200_OK)

# takeStock -> updatea el stock más viejo que tengamos del producto siempre y cuando exista alguno.
def takeStock(request, product_id):
  try:
    min_date_in = Stock.objects.filter(product=product_id, date_out__isnull=True).aggregate(min_date_in=Min('date_in'))['min_date_in']

    if min_date_in is None:
      return Response("No stock available for this product", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    stock_record = Stock.objects.filter(product=product_id, date_in=min_date_in, date_out__isnull=True).order_by('id').first()
    if stock_record is None:
      return Response('No stock record found for this product', status=status.HTTP_405_METHOD_NOT_ALLOWED)

    stock_record.date_out = timezone.now().date()
    stock_record.save()

    stock_data = {
      'product': stock_record.product.id,
      'date_in': stock_record.date_in,
      'date_out': stock_record.date_out,
    }

    return Response(stock_data, status=status.HTTP_200_OK)
  except Exception as e:
    return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)