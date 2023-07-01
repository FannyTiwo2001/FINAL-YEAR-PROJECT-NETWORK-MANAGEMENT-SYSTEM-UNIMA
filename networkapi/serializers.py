from rest_framework import serializers
from .models import Router, Interface, Switch, Port, MACTable
#class SubnetSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Subnet
   #     fields = ['id','name','ip']
class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Router
        fields = ['id','state','name', 'ip','community_string','temperature', 'uptime', 'memoryUtelization','interfaces']
class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ['id','name', 'ip','state', 'speed', 'interfaceType', 'description', 'macAddress', 'inputPacketCount', 'outputPacketCount', 'inputErrorCount', 'outputErrorCount', 'router']
class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        fields = ['id','name', 'ip','temperature','uptime','memoryUtelization']
class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ['id','portNumber','state', 'speed','inputPacketCount', 'outputPacketCount', 'inputErrorCount', 'outputErrorCount','vlanId','trunkSetting','duplexSetting' 'switch']