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
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView,)


from .views import *



urlpatterns = [
    path('test-api-view/', test_api_view),
    path('product-api-view/<int:pk>', product_api_view),
    path('product-api-view/', ProductListAPIView.as_view(), name='ListAPI'),
    path('product-api-view/create', ProductCreateAPIView.as_view(), name='CreateAPI'),
    path('product-api-view/update/<int:pk>', ProductUpdateAPIView.as_view(), name='UpdateAPI'),
    path('product-api-view/delete/<int:pk>', ProductDeleteAPIView.as_view(), name='DeleteAPI'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
