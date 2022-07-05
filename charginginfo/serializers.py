from rest_framework import serializers
from .models import Charginginfo

class CharginginfoSerializer(serializers.ModelSerializer):

  class Meta:
    model = Charginginfo
    fields = '__all__'