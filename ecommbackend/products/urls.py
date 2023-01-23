from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products',views.ProductViewSet,basename='products')
router.register('categories',views.CategoryViewSet,basename='categories')
# router.register('vendors',views.VendorsViewSet,basename='vendors')

urlpatterns=[
    path('',include(router.urls)),   
]