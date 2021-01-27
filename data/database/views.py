#from django.shortcuts import render
#from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

# Create your views here.



from .models import Table
from .refreshers import TableSerializer



class TablesViewSet(ModelViewSet):
	queryset = Table.objects.all()
	serializer_class = TableSerializer


