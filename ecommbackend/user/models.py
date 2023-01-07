from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserProfile(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)   
    user_country = models.CharField('Country',max_length=100,null=True,blank=True)
    user_city=models.CharField('City',max_length=100,null=True,blank=True)
    user_address=models.CharField('address',max_length=255,null=True,blank=True)
    gender_choices=(('male','Male'),('female','Female'),('other','Other'))
    user_gender=models.CharField('Gender',max_length=20,choices=gender_choices,default='male')
    is_vendor = models.BooleanField('Vendor',default=False)
    user_age = models.PositiveIntegerField('Age',validators=[MinValueValidator(18), MaxValueValidator(100)],null=True,blank=True)    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.username