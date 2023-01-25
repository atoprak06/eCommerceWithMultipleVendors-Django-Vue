from django.db import models
from user.models import UserProfile

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
    image_url = models.FileField(upload_to='product_images',default='pics/400x300.png')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comments(models.Model):
    product = models.OneToOneField(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='comments')  

    def __str__(self):
        return f"{self.product.title}-{self.product.id}"    
    class Meta:
        verbose_name_plural="comments"


    
class Comment(models.Model):
    comments= models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='comments')
    star_choices = ((0,'None'),(1,'Very Bad'),(2,'Bad'),(3,'Not Bad'),(4,'Good'),(5,'Very Good'))
    star = models.CharField(max_length=40,choices=star_choices,default=0)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=200,null=False,blank=False)

    class Meta:
        ordering=['-created_at']
        verbose_name_plural="comment"

    def __str__(self):
        return f"{self.user.username}'-'{self.created_at}"

