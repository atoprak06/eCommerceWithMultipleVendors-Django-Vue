from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(methods=['get','patch',],permission_classes=[IsAuthenticatedOrReadOnly],detail=True)
    def get_product(self,request,pk=None):
        product = Product.objects.get(id=pk)
        if product.created_by == request.user:
            request.data['id'] = pk
            Product.objects.filter(id=pk).update(**request.data)
            product =  Product.objects.get(id=pk)                
            serializer = ProductSerializer(product,many=False)
            return Response(serializer.data)
        else:
            return Response('product not found or you are not authorized')



class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()