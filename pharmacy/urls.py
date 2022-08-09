"""pharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView,)
from products.models import Product

from products.views import *


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', our_products_page, name='main_products'),
    path('asd/', search_product, name='search'),
    path('add/', add_product),
    path('medclass/', med_class, name='medclass'),
    path('medclass/add/', medclass_add, name='medclass-add'),
    path('medclass/edit/<int:pk>', medclass_add, name='medclass-edit'),
    path('medclass/delete/<int:pk>', med_class_delete, name='medclass-delete'),
    path('activeingredient/', ActiveIngredientListView.as_view(), name='activeingredient'),
    path('activeingredient/add', ActiveIngredientCreateView.as_view(), name='activeingredient-add'),
    path('activeingredient/edit/<int:pk>', ActiveIngredientUpdateView.as_view(), name='activeingredient-edit'),
    path('activeingredient/delete/<int:pk>', ActiveIngredientDeleteView.as_view(), name='activeingredient-delete'),
    path('product/', ProductListView.as_view(), name='product'),
    path('product/add', ProductCreateView.as_view(), name='product-add'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product-edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),
    path('register/', user_register_view, name='register'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
