from rest_framework import serializers 
from Main.models import *


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'