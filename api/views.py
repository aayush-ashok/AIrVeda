from typing import Final
from django.http.response import FileResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse


# Create your views here.
@api_view(['GET','DELETE'])
def DeleteOrRetrive(request,uid):
    dev = Device.objects.all().filter(uid=uid)
    if request.method=='DELETE':
        dev.delete()
        return Response("Succesfully Deleted UID: "+str(uid))
    elif request.method=='GET':
        serializer_pull = DeviceSerializer(dev,many=True)
        return Response(serializer_pull.data)



@api_view(['GET'])
def Visualization(request):
    
    uid = 2
    uid=request.GET.get('uid')
    TempData = pd.DataFrame(list(Temperatures.objects.all().filter(uid=uid).values()))
    HumiData = pd.DataFrame(list(Humidity.objects.all().filter(uid=uid).values()))
    
    fig,ax = plt.subplots()
    if len(TempData)>1:
        plt.plot(TempData['DateTime'],TempData['temperature'],label='Temperature')
    if len(HumiData)>1:
        plt.plot(HumiData['DateTime'],HumiData['humidity'],label='Humidity')
    
    if len(TempData)==0 & len(HumiData)==0:
        return HttpResponse("No Data Found for UID : -"+str(uid))
    
    plt.xlabel('Date Time')
    plt.ylabel('Value')
    plt.legend()
    fig.savefig('my_plot.png')
    
    return FileResponse(open('my_plot.png','rb'))





@api_view(['GET'])
def date_filter(request,uid,parameter):

    # devices = Device.objects.all()
    print(request.GET.get('start_on'),request.GET.get('end_on'))
    start_on = str(request.GET.get('start_on')).split('T')
    end_on = str(request.GET.get('end_on')).split('T')
    strt = start_on[0]+' '+start_on[1]
    endt = end_on[0]+' '+end_on[1]
    start = dt.strptime(strt,"%Y-%m-%d %H:%M:%S")
    end = dt.strptime(endt,"%Y-%m-%d %H:%M:%S")
    
    if parameter.upper() == 'TEMPERATURE':
        data = Temperatures.objects.all().filter(DateTime__range=[start,end])
        serializer_temp = TemperatureSerializer(data,many=True)
        return Response(serializer_temp.data)

    elif parameter.upper() == 'HUMIDITY':
        data = Humidity.objects.all().filter(DateTime__range=[start,end])
        serializer_temp = HumiditySerializer(data,many=True)
        return Response(serializer_temp.data)
    else:
        return Response('Incorrect Parameter Recieved. Parameters are - "Temperature" and "Humidity"')
    


@api_view(['GET','POST'])
def DeviceReq(request):
    if request.method == 'POST':
        serializer_push = DeviceSerializer(data=request.data)
        # print(serializer_push)
        if serializer_push.is_valid():
            serializer_push.save()
        return Response("Created New Device")
        
    else:
        devices = Device.objects.all()
        serializer_pull = DeviceSerializer(devices,many=True)
        
        return Response(serializer_pull.data)
    return