from django.db import models
class Router(models.Model):
    name = models.CharField(max_length=200,null=True,default=None)
    ip = models.CharField(max_length=200)
    community_string = models.CharField(max_length=100 , default="router" )
    temperature = models.CharField(max_length=200,null=True, default=None)
    uptime= models.CharField(max_length=200,null=True, default=None)
    memoryUtelization= models.CharField(max_length=200,null=True, default=None)
    interfaces = models.CharField(max_length=200,null=True, default=None)
    state = models.CharField(max_length=200,null=True, default=None)
    #subnet = models.ForeignKey(Subnet, on_delete=models.CASCADE)
    #cpu_utelization = models.FloatField(null=True,default=None)
    #Router has one to many relationship with Interface
    #The relationship is defined by foreign key of router in interface

class Interface(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200,null=True,default=None)
    state = models.CharField(max_length=200,default=None, null=True)
    speed = models.CharField(max_length=200,default=None, null=True)
    interfaceType = models.CharField(max_length=200,default=None, null=True)
    description = models.CharField(max_length=200,default=None, null=True)
    macAddress = models.CharField(max_length=200, null=True, default=None)
    inputPacketCount = models.CharField(max_length=200,default=None, null=True)
    outputPacketCount = models.CharField(max_length=200,default=None, null=True)
    inputErrorCount = models.CharField(max_length=200,default=None, null=True)
    outputErrorCount = models.CharField(max_length=200,default=None, null=True)
    router = models.ForeignKey(Router, on_delete=models.CASCADE)


class Switch(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    temperature = models.FloatField(null=True, default=None)
    uptime = models.IntegerField(null=True, default=None)
    memoryUtelization = models.IntegerField(null=True, default=None)
    #subnet = models.ForeignKey(Subnet, on_delete=models.CASCADE)
    #Switch has one to many relationship with Ports

class Port(models.Model):
    portNumber = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    speed = models.IntegerField(null=True, default=None)
    inputPacketCount = models.IntegerField(null=True, default=None)
    outputPacketCount = models.IntegerField(null=True, default=None)
    inputErrorCount = models.IntegerField(null=True, default=None)
    outputErrorCount = models.IntegerField(null=True, default=None)
    vlanId = models.IntegerField(null=True, default=None)
    trunkSetting = models.BooleanField(default=False)
    duplexSetting = models.CharField(max_length=200, null=True, default=None)
    #Port has a relationship with switch and a mac table
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)

class MACTable(models.Model):
    macAddress = models.CharField(max_length=200,default=None)
    vlan = models.IntegerField(null=True,default=None)
    typeOf = models.CharField(max_length=200,null=True, default=None)
    age = models.IntegerField(null=True, default=None)
    securityViolation = models.BooleanField(default=False)
    secureMac = models.BooleanField(default=False)
    switch = models.ForeignKey(Switch, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)