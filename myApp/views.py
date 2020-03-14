from django.shortcuts import render
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.conf import settings
import json

@api_view(['POST'])
def IdealWeight(heigthdata):
    try:
        height = json.loads(heigthdata.body)
        weigth = height * 10
        return JsonResponse("Ideal weigth should be " + str(weigth),safe=False)
    except ValueError as err:
        return Response(err.args[0],status.HTTP_400_BAD_REQUEST)