from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Fruit(models.Model):
    name = models.CharField(max_length=32, verbose_name="Fruits", blank=False)
    expire_date = models.CharField(
        max_length=12, verbose_name="ExpireDate", blank=False)
    image = models.FileField(verbose_name="Image",
                             upload_to="documents/%Y/%m/%d")
    category = models.CharField(
        verbose_name="Category", max_length=40, default="Default")
    quantity = models.FloatField(verbose_name="Quantity", default=1)
    unit = models.CharField(verbose_name="Unit", max_length=40, default="KG")
    isExpired = models.BooleanField(verbose_name="IsExpired", default=False)
    barcode = models.CharField(
        max_length=120, verbose_name="Barcode", blank=True,unique=True)

    class Meta:
        verbose_name = "Fruit"
        verbose_name_plural = "Fruits"

    def __str__(self):
        return str(self.name + " "+self.expire_date + " "+self.category)


class UsersFruits(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User', unique=False)
    fruit = models.OneToOneField(Fruit, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "User-Fruit"
        verbose_name_plural = "User-Fruits"

    def __str__(self):
        return str(self.user.username + " " + self.fruit.name)


class UserCart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="User")
    fruit = models.OneToOneField(
        Fruit, on_delete=models.CASCADE, verbose_name="Fruit", unique=True)

    class Meta:
        verbose_name = "User-Cart"
        verbose_name_plural = "User-Carts"

    def __str__(self):
        return str(self.user.username + " "+self.fruit.name)
