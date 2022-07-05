from rest_framework import serializers
from charginginfo.models import Charginginfo

class CharginginfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Charginginfo
    fields = '__all__'