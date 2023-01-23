from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category
from user.models import UserProfile
from user.serializers import UserShowSerializerVendor
from django.template.defaultfilters import slugify
from django.db.models import Prefetch
import django_filters 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['category','product_state','created_by__username','title']



class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    # filterset_fields = ['category','product_state','created_by__username','title']
  

    def perform_create(self, serializer):        
        serializer.save(created_by=self.request.user,slug=slugify(self.request.data['title']))        
    
    # def list(self,request):
    #     products = Product.objects.filter(product_state='active',created_by__is_vendor=True)
    #     serializer= ProductSerializer(products,many=True)
    #     return Response(serializer.data)       
    
    @action(detail=False)
    def my_products(self,request):
        products = Product.objects.filter(created_by=request.user)
        serializer= ProductSerializer(products,many=True)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(serializer.data, request)
        if page is not None:
            return paginator.get_paginated_response(page)
        return Response(serializer.data)

# class VendorsViewSet(viewsets.ReadOnlyModelViewSet):
#     serializer_class = UserShowSerializerVendor
#     permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['username']
  
#     def get_queryset(self):
#         queryset=UserProfile.objects.prefetch_related(Prefetch('products',queryset=Product.objects.filter(product_state='active'))).filter(is_vendor=True)           
#         username = self.request.query_params.get('username')
#         queryset.filter(username=username)        
#         return queryset

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
