from rest_framework import serializers
from .models import user

class DataSerialzer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = user
		fields = ('id','username','firstname','lastname','DOB','mobile','address','state','country')