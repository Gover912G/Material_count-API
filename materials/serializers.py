from rest_framework import serializers
from .models import Router, ONU, DropCable, DropCableUsageRecord


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = '__all__'

class ONUSerializer(serializers.ModelSerializer):
    class Meta:
        model = ONU
        fields = '__all __'

class DropCableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCable
        fields = '__all__'

class DropCableUsageRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropCableUsageRecord
        fields = '__all__'