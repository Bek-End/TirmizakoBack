from django.contrib import admin
from main.models import Fruit, UsersFruits,UserCart

# Register your models here.
admin.site.register(Fruit)
admin.site.register(UsersFruits)
admin.site.register(UserCart)