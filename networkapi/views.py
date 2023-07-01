from django.http import JsonResponse, HttpRequest
from .models import Router, Interface, Switch, Port
from .serializers import RouterSerializer, InterfaceSerializer ,SwitchSerializer,PortSerializer #SubnetSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
from concurrent.futures import ThreadPoolExecutor
from .router import Router as ruta

@api_view(['GET'])
def getAllRouters(request):
    if request.method == 'GET':
        router = Router.objects.all()
        serializer=RouterSerializer(router, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
#def create_subnet(request):
  #  if request.method == 'POST':
   #     serializer =SubnetSerializer(data=request.data)
    #    if serializer.is_valid():
     #       serializer.save()
      #      return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def create_router(request):
    if request.method == 'POST':
        serializer = RouterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def create_interface(request):
    if request.method == 'POST':
        serializer = InterfaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET'])
def get_interface_by_id(request, id):
    if request.method== 'GET':
        try:
            interface= Interface.objects.get(router=id)

        except Interface.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InterfaceSerializer(interface, many=True)
        return JsonResponse(serializer.data, safe=False)
@api_view(['POST'])
def create_switch(request):
    if request.method == 'POST':
        serializer=SwitchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
@api_view(['POST'])
def create_port(request):
    if request.method == 'POST':
        serializer=PortSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
@api_view(['GET'])
def get_switch(id):
    try:
        switch = Switch.objects.get(pk=id)
    except Switch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = SwitchSerializer(switch, many=True)
    return JsonResponse(serializer.data, safe=False)
@api_view(['GET'])
def get_port_by(id):
    try:
        port = Port.objects.get(switch=id)
    except Switch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PortSerializer(port, many=True)
    return JsonResponse(serializer.data, safe=False)
@api_view(['GET'])
def get_router(id):
    try:
        switch = Router.objects.get(pk=id)
    except Switch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RouterSerializer(switch, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def start_monitoring_router(request,id):
    #try:
    r = ruta(id)
    #except:
        #return JsonResponse({'message':"No Router with such id"})
    r.monitor_router
    return JsonResponse({'message':"Monitoring Started"})
@api_view(['GET'])
def stop_router_monitoring(request):
    return JsonResponse({'message':"Monitoring Stopped"})