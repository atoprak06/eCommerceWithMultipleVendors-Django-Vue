from django.core.management.base import BaseCommand
from faker import Faker
import random
from user.models import UserProfile
from ...models import Product,Category
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Generate random product data'

    def handle(self, *args, **options):
        fake = Faker()
        choices_list = ['active','deactive']     
        for _ in range(500):
            title=str(fake.name()).strip('(),')                       
            Product.objects.create(
                category=random.choice(Category.objects.all()),
                created_by=random.choice(UserProfile.objects.all()),
                title=title,              
                slug=slugify(title),
                description=fake.paragraph(),
                price=fake.random_number(digits=3),
                product_state=random.choice(choices_list),                            
            )
        self.stdout.write(self.style.SUCCESS('Successfully generated random product data'))