from rest_framework import serializers
from .models import Category,Product,Comment
from user.models import UserProfile

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='title')
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model= Product        
        fields = '__all__'
        read_only_fields = ['id','created_by']

    # def to_representation(self, instance):
    #     rep = super(ProductSerializer, self).to_representation(instance)
    #     rep['category'] = instance.category.title
    #     rep['created_by'] = instance.created_by.username
    #     return rep

class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    class Meta:
        model= Category
        fields = ('title','id')
        read_only_fields = ['id',]

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=UserProfile.objects.all(),slug_field='username')    
    class Meta:
        model=Comment
        fields = ('id','star','created_at','comment','user')
        read_only_fields = ['id','user']
