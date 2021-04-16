from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Fruit


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username")

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = '__all__'