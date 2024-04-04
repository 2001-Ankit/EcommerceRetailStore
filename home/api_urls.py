# Routers provide an easy way of automatically determining the URL conf.
from rest_framework import routers
from .views import  *
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('filter_product', ProductFilterViewSet.as_view(), name='products'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]