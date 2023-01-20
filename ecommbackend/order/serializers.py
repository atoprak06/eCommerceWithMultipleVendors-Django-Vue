from rest_framework import serializers
from .models import Order,OrderItem
from products.serializers import ProductSerializer
from user.models import UserProfile


class OrderItemSerializer(serializers.ModelSerializer):
    product= ProductSerializer(many=False)
    class Meta:
        model=OrderItem
        fields=['product','created_at','quantity','productTotalPrice']

class OrderSerializer(serializers.ModelSerializer):    
    products = OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['id','created_at','orderTotalPrice','products']

class OrderProductSerializer(serializers.ModelSerializer):
    customer = serializers.SlugRelatedField(many=False,slug_field='username',queryset=UserProfile.objects.all())    
    class Meta:
        model=Order 
        fields=['customer','id'] 

class OrderedItemSerializer(serializers.ModelSerializer):    
    order = OrderProductSerializer(many=False)
    product = ProductSerializer(many=False)
    class Meta:
        model=OrderItem
        fields=['order','created_at','quantity','productTotalPrice','product']
        

