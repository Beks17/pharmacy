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

from products.views import our_products_page


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

def search_product(request):
    search_text = request.GET.get('search-text')

    html = "Salom olam"
    
    for item in Product.objects.all(): 
        if search_text.lower() in item.name.lower():
            html += f"""
                <div class="column {item.med_class} show">
                    <div class="content">
                    <img src="{item.med_image}" alt="{item.med_class}" style="width:100%">
                    <h4>{item.name}</h4>
                    <p>{item.reg_num}</p>
                    </div>
                </div>
                """
    html += '<br>'
    return HttpResponse(html)
# <div class="search">

#   {% for item in search %}
#   <div class="column {{item.med_class}} show">
#       <div class="content">
#           <img src="{{item.med_image}}" alt="{{item.med_class}}" style="width:100%">
#           <h4>{{item.name}}</h4>
#           <p>{{item.reg_num}}</p>
#       </div>
#   </div>
#   {% endfor %}

# </div> 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', our_products_page),
    path('asd/', search_product),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
