from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CharginginfoSerializer

from charginginfo.models import Charginginfo

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List':'/charginginfo-list/',
    'Detail View':'/charginginfo-detail/<str:pk>/',
    'Create':'/charginginfo-create/',
    'Update':'/charginginfo-update/<str:pk>/',
    'Delete':'/charginginfo-delete/<str:pk>/',
    }

  return Response(api_urls)

@api_view(['GET'])
def charginginfoList(request):
  charginginfos = Charginginfo.objects.all()
  serializer = CharginginfoSerializer(charginginfos, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def charginginfoDetail(request, pk):
  charginginfos = Charginginfo.objects.get(id=pk)
  serializer = CharginginfoSerializer(charginginfos, many=False)

  return Response(serializer.data)

@api_view(['POST'])
def charginginfoCreate(request):
  serializer = CharginginfoSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['POST'])
def charginginfoUpdate(request, pk):
  charginginfo = Charginginfo.objects.get(id=pk)
  serializer = CharginginfoSerializer(instance=charginginfo, data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def charginginfoDelete(request, pk):
  charginginfo = Charginginfo.objects.get(id=pk)
  charginginfo.delete()

  return Response("Item is successfully deleted!")