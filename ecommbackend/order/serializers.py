from rest_framework import serializers
from products.models import Category,Product
from .models import Order,OrderItem
from user.models import UserProfile


class OrderSerializer(serializers.ModelSerializer):
    # products=OrderItemSerializer(many=True)
    customer = serializers.SlugRelatedField(many=False,slug_field='username',queryset=UserProfile.objects.all())
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields = ['id']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'
        read_only_fields = ['id']

