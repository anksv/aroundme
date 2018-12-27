from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json
from db.collection import databaseServices
from utility.helper import commonData
from .models import Location
from .serializer import LocationSerializer

dbb = databaseServices()
cd = commonData()

# @api_view(["POST"])
# def savelocations(request):
#     request_json = cd.map_json(request.body)
#     response = dbb.savelocations(cd.db_name,cd.db_collection,request_json)
#     return HttpResponse(cd.convert_to_json(response))

@api_view(["POST"])
def savelocations(request):
    serializer = LocationSerializer(data=request.data,many=True)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("Inserted data Successfully")
    return HttpResponse(serializer.errors)

@api_view(["GET"])
def getlocations(request):
    queryset = Location.objects.all()
    serializer = LocationSerializer(queryset, many=True)
    return HttpResponse(cd.convert_to_json(serializer.data))

@api_view(["GET"])
def getcurrentlocation(request):
    return HttpResponse