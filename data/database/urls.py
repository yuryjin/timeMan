from django.urls import path

from rest_framework import routers

from .views import *

#from .views import index

router = routers.DefaultRouter()
router.register('tables', TablesViewSet)


urlpatterns = router.urls