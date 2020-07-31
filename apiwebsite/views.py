from django.db import transaction
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
import random,string
from rest_framework.response import Response
from rest_framework import status
from .models import DataNumber,CurrentNumber
from .serializer import GetChartTwotModelSerializer


class GetChartOneAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data_list_str=random.sample(string.digits, 5)
        data_list_int = list(map(int,data_list_str))
        numbers = " ".join(data_list_str)
        bools = DataNumber.objects.first()
        if not bools:
            try:
                with transaction.atomic():
                    DataNumber.objects.create(number=numbers)
            except:
                return Response("获取数据失败", status=status.HTTP_400_BAD_REQUEST)

        return Response(data_list_int,status=status.HTTP_200_OK)
class UpdateChartOneAPIView(APIView):
    def post(self,request,*args,**kwargs):
        data_list_str = random.sample(string.digits, 5)
        data_list_int = list(map(int, data_list_str))

        numbers = " ".join(data_list_str)
        try:
            with transaction.atomic():
                data=DataNumber.objects.first()
                data.number=numbers
                data.save()
        except:
            return Response("数据更新失败",status=status.HTTP_400_BAD_REQUEST)
        return Response(data_list_int,status=status.HTTP_200_OK)

class SaveChartTwoAPIView(APIView):
    def post(self,request,*args,**kwargs):
        data=request.data["data"]
        data_list_str = list(map(str, data))
        numbers = " ".join(data_list_str)
        bools=CurrentNumber.objects.filter(currentNumber=numbers)
        print(bools)
        if not bools:
            try:
                with transaction.atomic():

                    CurrentNumber.objects.create(currentNumber=numbers)
                    return Response("保存成功！", status=status.HTTP_200_OK)
            except:
                return Response("保存数据失败", status=status.HTTP_400_BAD_REQUEST)
        return Response("数据已存在", status=status.HTTP_400_BAD_REQUEST)




class GetChartTwoAPIView(APIView):
    def get(self,request,*args,**kwargs):
        series=[]
        cur_data = CurrentNumber.objects.all()[:100] #最大显示一百条数据
        for i in cur_data:
            series.append({"data":list(map(int,i.currentNumber.split(" ")))})
        return_data={"series":series,"sigle_number":[i for i in range(1,len(series[0]["data"])+1)]}
        return Response(return_data,status=status.HTTP_200_OK)



        # pn=GetChartTwoSetPagination()#分页
        # res = pn.paginate_queryset(cur_data, request=request, view=self)
        # page = GetChartTwotModelSerializer(res, many=True)
        # for i in page.data:
        #     print(i["currentNumber"])
        #     series.append({"data": list(map(int, i["currentNumber"].split(" ")))})
        # return_data = {"series": series, "sigle_number": [i for i in range(1, len(series[0]["data"]) + 1)]}
        # return pn.get_paginated_response(return_data)


