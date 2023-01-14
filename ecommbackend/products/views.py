from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category
from user.models import UserProfile
from user.serializers import UserShowSerializer
from django.template.defaultfilters import slugify
from django.db.models import Prefetch


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]  

    def perform_create(self, serializer):        
        serializer.save(created_by=self.request.user,slug=slugify(self.request.data['title']))
        
    
    def list(self,request):
        products = Product.objects.filter(product_state='active')
        serializer= ProductSerializer(products,many=True)
        return Response(serializer.data)
       
    
    @action(detail=False)
    def my_products(self,request):
        products = Product.objects.filter(created_by=request.user)
        serializer= ProductSerializer(products,many=True)
        return Response(serializer.data)

class VendorsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserShowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    
    def get_queryset(self):
        return UserProfile.objects.filter(is_vendor=True) 

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related(Prefetch('products',queryset=Product.objects.filter(product_state='active')))    
    permission_classes = [IsAuthenticatedOrReadOnly]
