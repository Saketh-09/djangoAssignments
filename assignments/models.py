from django.db import models

# Create your models here.

class ShopingItem(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    discount = models.IntegerField()
    expirydate = models.DateTimeField(null = True)

    def __str__(self):
        return self.name

# a = [0]*3

# for i in range(3):
#     a[i] = ShopingItem.objects.create(name = 'Item'+str(i), price = i*10, discount = 5)
#     a[i].save()
    
# print(ShopingItem.objects.all())   
