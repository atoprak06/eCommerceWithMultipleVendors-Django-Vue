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

class OrderedItemSerializer(OrderItemSerializer):    
    class Order(OrderSerializer):
        customer =  serializers.SlugRelatedField(many=False,slug_field='username',queryset=UserProfile.objects.all())   
        class Meta(OrderSerializer.Meta):
            fields=['customer','id']
    order = Order(many=False)    
    class Meta(OrderItemSerializer.Meta):                
        fields=['order','created_at','quantity','productTotalPrice','product']
        

