from djoser.serializers import UserCreatePasswordRetypeSerializer
from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import UserProfile
from products.models import Product
from products.serializers import ProductSerializer

class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender','password')

class UserShowSerializerVendor(UserSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender','products')
        read_ony_fields = ['products',]


class UserShowSerializerEdit(UserSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender',)
        

