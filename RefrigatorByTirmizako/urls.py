from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import SignUp, SignIn, AddFruit, UpdateFruit, RemoveFruit, UserCartAddProduct, UserCartRemoveProduct, CheckExpiration, ProductsGetExpired, ProductsGetFresh, ProductsGetByCategory, ProductsGetAll, RemoveByBarCode, UserCartGetProducts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/sign-up', SignUp.as_view(), name="SignUp"),
    path('auth/sign-in', SignIn.as_view(), name="SignIn"),
    path('products/add', AddFruit.as_view(), name="AddFruit"),
    path('products/update', UpdateFruit.as_view(), name="UpdateFruit"),
    path('products/delete', RemoveFruit.as_view(), name="RemoveFruit"),
    path('cart/add', UserCartAddProduct.as_view(), name="AddToCart"),
    path('cart/remove', UserCartRemoveProduct.as_view(), name="RemoveFromCart"),
    path('expiration/check', CheckExpiration.as_view(), name="CheckExpiration"),
    path('expiration/get_expired_products',
         ProductsGetExpired.as_view(), name="ExpiredProducts"),
    path('expiration/get_fresh', ProductsGetFresh.as_view(), name="FreshProducts"),
    path('expiration/get_by_category/<category>',
         ProductsGetByCategory.as_view(), name="CategoryProducts"),
    path('expiration/get_all', ProductsGetAll.as_view(), name="ProductsAll"),
    path('products/remove_barcode',
         RemoveByBarCode.as_view(), name="RemoveByBarcode"),
    path('cart/get_products', UserCartGetProducts.as_view(), name="GetCartProducts")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
