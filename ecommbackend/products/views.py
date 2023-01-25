from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import ProductSerializer,CategorySerializer,CommentSerializer
from .models import Product,Category,Comment,Comments
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


class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = { 
        'default': None,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

class ProductViewSet(MultiSerializerViewSet):
    serializers ={
        'default' : ProductSerializer,
        'comments': CommentSerializer,    
    }     
    queryset = Product.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def perform_create(self, serializer):        
        serializer.save(created_by=self.request.user,slug=slugify(self.request.data['title']))        
   
    
    @action(detail=False)
    def my_products(self,request):
        products = Product.objects.filter(created_by=request.user)
        serializer= ProductSerializer(products,many=True)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(serializer.data, request)
        if page is not None:
            return paginator.get_paginated_response(page)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get','post',],permission_classes=[IsAuthenticatedOrReadOnly])
    def comments(self,request,pk=None):
        product = Product.objects.get(id=pk)
        comments=Comments.objects.get_or_create(product=product)
        if request.method == 'GET':            
            comment = Comment.objects.filter(comments=comments[0])
            serializer = CommentSerializer(comment,many=True)
            paginator = pagination.PageNumberPagination()
            page = paginator.paginate_queryset(serializer.data, request)
            if page is not None:                
                return paginator.get_paginated_response(page)            
            return Response(serializer.data)
        if request.method == 'POST':
            comment = Comment.objects.create(user=self.request.user,comments=comments[0],star=request.data['star'],comment=request.data['comment'])
            serializer = CommentSerializer(comment,many=False)
            return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
