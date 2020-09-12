from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('userview', views.UserViewSet)
router.register('producerprofileview', views.ProducerProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
  
]