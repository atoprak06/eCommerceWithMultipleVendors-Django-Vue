from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('order',views.OrderViewSet,basename='order')

urlpatterns=[
    path('',include(router.urls)),
]