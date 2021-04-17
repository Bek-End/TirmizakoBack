from rest_framework.views import APIView
from rest_framework.response import Response
from basicauth import decode, encode
from django.contrib.auth import authenticate
from rest_framework import status
from django.contrib.auth.models import User
from main.models import Fruit, UsersFruits, UserCart
from datetime import datetime
from main.serializers import FruitSerializer

# Create your views here.


class SignIn(APIView):
    @staticmethod
    def post(request):
        username = request.data["username"]
        password = request.data["password"]
        print(username, password)
        account = authenticate(username=username, password=password)
        print(account)
        if(account is not None):
            return Response({"Token": encode(username, password)}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class SignUp(APIView):
    @staticmethod
    def post(request):
        username = request.data["username"]
        password = request.data["password"]
        print(username, password)
        User.objects.create_user(username=username, password=password)
        return Response(status=status.HTTP_201_CREATED)


class AddFruit(APIView):
    @staticmethod
    def post(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        if(account is not None):
            name = request.data["name"]
            expire_date = request.data["expire_date"]
            image = request.FILES["file"]
            cat = request.data["category"]
            quantity = request.data["quantity"]
            unit = request.data['unit']
            if request.data['barcode'] is not None:
                barcode = request.data['barcode']
                fruit = Fruit.objects.create(
                    name=name, expire_date=expire_date, image=image, category=cat, quantity=quantity, unit=unit, barcode=barcode)
            else:
                fruit = Fruit.objects.create(
                    name=name, expire_date=expire_date, image=image, category=cat, quantity=quantity, unit=unit)
            UsersFruits.objects.create(user=account, fruit=fruit)
            print(fruit.name)
            return Response({
                "fruit_id": fruit.id,
                "image_url": fruit.image.url,
                "name": str(fruit.name),
                "expire_date": fruit.expire_date,
                "category": fruit.category,
                "is_expired": fruit.isExpired
            },
                status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class RemoveFruit(APIView):
    @staticmethod
    def delete(request):
        username, password = decode(request.headers['Authorization'])
        fruit_id = int(request.data["fruit_id"])
        account = authenticate(username=username, password=password)
        if(account is not None):
            fruit = Fruit.objects.get(pk=fruit_id)
            fruit.image.delete(save=True)
            fruit.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class RemoveByBarCode(APIView):
    @staticmethod
    def delete(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        barcode = int(request.data["barcode"])
        if(account is not None):
            fruit = Fruit.objects.get(barcode=barcode)
            fruit.image.delete(save=True)
            fruit.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UpdateFruit(APIView):
    @staticmethod
    def post(request):
        username, password = decode(request.headers['Authorization'])
        fruit_id = int(request.data["fruit_id"])
        name = request.data["name"]
        expire_date = request.data["expire_date"]
        image = request.FILES["file"]
        cat = request.data["category"]
        quantity = request.data["quantity"]
        unit = request.data['unit']
        account = authenticate(username=username, password=password)
        if(account is not None):
            fruit = Fruit.objects.get(pk=fruit_id)
            fruit.image.delete(save=True)
            fruit.expire_date = expire_date
            fruit.name = name
            fruit.image = image
            fruit.category = cat
            fruit.unit = unit
            fruit.quantity = quantity
            fruit.save()
            return Response(
                {
                    "fruit_id": fruit.id,
                    "image_url": fruit.image.url,
                    "name": fruit.name,
                    "expire_date": fruit.expire_date,
                    "category": fruit.category,
                    "is_expired": fruit.isExpired
                },
                status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserCartAddProduct(APIView):
    @staticmethod
    def post(request):
        username, password = decode(request.headers['Authorization'])
        fruit_id = int(request.data["fruit_id"])
        account = authenticate(username=username, password=password)
        if(account is not None):
            fruit = Fruit.objects.get(pk=fruit_id)
            UserCart.objects.create(user=account, fruit=fruit)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserCartRemoveProduct(APIView):
    @staticmethod
    def delete(request):
        username, password = decode(request.headers['Authorization'])
        fruit_id = int(request.data["fruit_id"])
        account = authenticate(username=username, password=password)
        if(account is not None):
            fruit = Fruit.objects.get(pk=fruit_id)
            item = UserCart.objects.get(fruit=fruit)
            item.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductsGetExpired(APIView):
    @staticmethod
    def get(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        if(account is not None):
            products = Fruit.objects.filter(isExpired=True)
            expiredProducts = FruitSerializer(products, many=True)
            return Response({"products": expiredProducts.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductsGetFresh(APIView):
    @staticmethod
    def get(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        if(account is not None):
            products = Fruit.objects.filter(isExpired=False)
            expiredProducts = FruitSerializer(products, many=True)
            return Response({"products": expiredProducts.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductsGetByCategory(APIView):
    @staticmethod
    def get(request, category):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        if(account is not None):
            products = Fruit.objects.filter(category=category)
            catProducts = FruitSerializer(products, many=True)
            return Response({"products": catProducts.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductsGetAll(APIView):
    @staticmethod
    def get(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        if(account is not None):
            products = Fruit.objects.all()
            catProducts = FruitSerializer(products, many=True)
            return Response({"products": catProducts.data}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class CheckExpiration(APIView):
    @staticmethod
    def post(request):
        username, password = decode(request.headers['Authorization'])
        account = authenticate(username=username, password=password)
        day, month, year = (request.data["today"]).split(".")
        print(day, month, year)
        if(account is not None):
            fruits = Fruit.objects.all()
            for fruit in fruits.iterator():
                exDay, exMonth, exYear = fruit.expire_date.split(".")
                today = datetime(
                    day=int(day), month=int(month), year=int(year))
                exPireDate = datetime(
                    day=int(exDay), month=int(exMonth), year=int(exYear))
                if(today >= exPireDate):
                    fruit.isExpired = True
                    fruit.save()
                    print("cool")
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
