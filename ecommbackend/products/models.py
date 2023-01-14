from django.db import models
from user.models import UserProfile
from django.template.defaultfilters import slugify
from faker import Faker
fake=Faker()

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField(max_length=255,null=True,blank=True)
    product_state_choices = (('active','Active'),('deactive','Deactive'))
    product_state = models.CharField(max_length=40,choices=product_state_choices,default='active')
    image_url = models.CharField(max_length=255,default=fake.image_url())

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title