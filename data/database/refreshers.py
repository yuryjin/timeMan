from rest_framework.serializers import ModelSerializer

from .models import Table
#from .models2 import Table2 'start', 'end'

class TableSerializer(ModelSerializer):
	class Meta:
		model = Table
		fields = ['id', 'event', 'start', 'end']

