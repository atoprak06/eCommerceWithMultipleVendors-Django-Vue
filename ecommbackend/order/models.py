from django.db import models
from user.models import UserProfile
from products.models import Product

class Order(models.Model):
    customer=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    orderTotalPrice=models.FloatField(null=True,blank=False)

    def __str__(self):
        return f'{self.customer.username} - {str(self.created_at)}'

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='products')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveIntegerField()
    productTotalPrice=models.FloatField()

    def __str__(self):
        return f'{self.product.title} - {str(self.created_at)}'
