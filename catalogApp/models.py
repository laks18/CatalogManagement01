from django.db import models
from django.contrib.auth.models import User
import datetime
from example_package_x21207232 import example

# Create your models here.
USERSTATUS = ((1, "Active"), (2, "Inactive"))
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=USERSTATUS, default=1, null=True, blank=True)
    company_code = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    office_address = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    work_location = models.CharField(max_length=100, null=True, blank=True)
    work_desk = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    image  = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Product_Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    createdby = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Product_Master(models.Model):
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    desc = models.TextField(null=True, blank=True)
    detaildesc = models.TextField(null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    createdby = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)
    extra_field = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def incrementprice(self):
        return self.price + (105/100)
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product_Master, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='product/', null=True)
    
    def __str__(self):
        return self.product.name
    
class ProductHistory(models.Model):
    productid = models.CharField(max_length=100, null=True, blank=True)
    productcategoryid = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.productid
    
ORDERSTATUS = ((1, "Pending for verification"), (2, "Approved/Delivered"), (3, "Cancel"), (4, "Return"), (5, 'Penalty'))
class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    orderid = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(Product_Master, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=ORDERSTATUS, default=1)
    country = models.CharField(max_length =100, null=True, blank=True)
    state = models.CharField(max_length =100, null=True, blank=True)
    zipcode = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length =100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    expiry_date = models.DateTimeField(auto_now_add=True, blank=True)
    penalty = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id)

    def remaining_days(self):
        print(datetime.date.today(), self.created.strftime('%B %d %Y'))
        remain_day = datetime.datetime.strptime(self.created.strftime('%B %d %Y'), '%B %d %Y').date()+datetime.timedelta(days=5) - datetime.date.today() 
        return remain_day.days

    def penaltydays(self):
        print(datetime.date.today(), self.created.strftime('%B %d %Y'))
        remain_day = datetime.datetime.strptime(self.created.strftime('%B %d %Y'), '%B %d %Y').date()+datetime.timedelta(days=5) - datetime.date.today() 
        print(remain_day);
        print("Inside penaltyDays")
        example.calcPenalty(remain_day.days);        
        
def calcPenalty(remain_day):
    print("Into calcPenalty")
    penaltyday = remain_day.days*(-1)
    if penaltyday < 0:
        return "no fine yet"
    else:
        return penaltyday
    
class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    productid = models.TextField(null=True, blank=True)
    quantity = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user.user.username
    
class Review(models.Model):
    product = models.ForeignKey(Product_Master, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    ranking = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.user.username
    
# class Country_Master(models.Model):
#     country_code=models.CharField(max_length=100, null=True, blank=True)    
#     country_name=models.CharField(max_length=100, null=True, blank=True)
#     country_currency=models.CharField(max_length=100, null=True)
#     country_flag=models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.country_name
    