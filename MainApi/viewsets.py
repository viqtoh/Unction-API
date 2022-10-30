
from rest_framework import viewsets
from .serializers import DataSerialzer
from .models import user
 
 
class userviewsets(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = DataSerialzer