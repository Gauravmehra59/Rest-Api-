from functools import partial
from django.urls import is_valid_path
from html5lib import serialize
from requests import request
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from app.models import TimingTodo, Toda
from .serializers import TodoSerializers, timingtodoserializer
from rest_framework import status,viewsets

from app import serializers


@api_view(['GET','POST','PATCH'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Hello, world!"})
    elif request.method == 'GET':
        return Response({"message": "Hello, Get"})
    elif request.method == 'PATCH':
        return Response({"message": "Hello, Patch"})
    else:
        return Response({"status": 400,
                        "message": "No Data method found",
                        })


@api_view(['GET'])
def get_todo(request):
    toda_obj = Toda.objects.all()
    serialize = TodoSerializers(toda_obj, many=True)
    return Response({
        "status" : "200",
        "massage" : "Sucessfully fetch the data",
        "data": serialize.data
    })


@api_view(['POST'])
def postt_todo(request):
    try:
        data = request.data
        serialize = TodoSerializers(data=data)
        if serialize.is_valid():
            serialize.save()
            return Response({"message": "sucess data",
                                "data":serialize.data})
        return Response({"message": "invalid data","data":serialize.data})
    except Exception as e:
        print(e)
    return Response({"message": "Something wrong"})

@api_view(["PATCH"])
def patch_data(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status' : False,
                'message' : 'uid is required',
                'data' : {}
            })
        obj = Toda.objects.get(uid=data.get('uid'))
        serializer = TodoSerializers(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status':True,
                'message':'sucess data',
                'data': serializer.data,
            })
        else:
            return Response({
                'status':False,
                'message':'invalid data',
                'data':serializer.data,
            })
    except Exception as e:
        return Response({
                'status':False,
                'message':'uid invalid ',
                'data':{},
            })


class todoviewset(viewsets.ModelViewSet):
    queryset = Toda.objects.all()
    serializer_class = TodoSerializers

    @action(detail=False, methods=['GET'])
    def get_timing_todo(self,request):
        objs = TimingTodo.objects.all()
        serialize = timingtodoserializer(objs , many=True)
        return Response({
            "status":True,
            "message":"Timing todo fetching",
            "data" : serialize.data
        })



    @action(detail=False, methods=['POST'])
    def add_date_to_todo(self,request):
        try:
            data = request.data
            serializers = timingtodoserializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response({"message": "sucess data",
                                "data":serializers.data})
            else:
                return Response({"message": "invalid data",
                                "data":serializers.errors})
        except Exception as e:
            print(e)
            # return Response({"message": "enter the data",
            #                     "data":serializers.errors})

        return Response({"status": False,
                        "message":"something wrong"
                            })
                



