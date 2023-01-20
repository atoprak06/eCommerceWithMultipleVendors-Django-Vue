from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import OrderItemSerializer,OrderSerializer,OrderedItemSerializer
from products.models import Product,Category
from .models import Order,OrderItem
# from user.serializers import UserShowSerializerVendor
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes=[IsAuthenticated] 

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def create(self, request, *args, **kwargs):        
        order = Order.objects.create(customer=request.user,orderTotalPrice= float(request.data['orderTotalPrice']))
        cartProducts = request.data['cartProducts']
        for product in cartProducts:            
            quantity=product['quantity']
            productTotalPrice = product['priceTotal']                      
            OrderItem.objects.create(product=Product.objects.get(id=product['id']) ,order=order,quantity=quantity,productTotalPrice=productTotalPrice)                                  
        serializer=OrderSerializer(order,many=False)
        return Response(serializer.data)
    
    @action(detail=False)
    def orderedProducts(self,request):
        queryset = OrderItem.objects.filter(product__created_by=self.request.user)
        serializer = OrderedItemSerializer(queryset,many=True)
        return Response(serializer.data)


