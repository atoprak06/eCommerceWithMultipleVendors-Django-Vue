from djoser.serializers import UserCreatePasswordRetypeSerializer
from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import UserProfile
from products.models import Product

class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender','password')

class UserShowSerializer(UserSerializer):
    products = serializers.SlugRelatedField(many=True,queryset=Product.objects.all(),slug_field='title')
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender','products')
