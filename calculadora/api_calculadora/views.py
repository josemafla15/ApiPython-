import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions



# Create your views here.
class SumaView(APIView):

    def get(self, request, *args, **kwargs):
        num_uno = request.GET.get('num_uno')
        num_dos = request.GET.get('num_dos')
        suma = int(num_uno) + int(num_dos)
        
        return Response(suma, status=status.HTTP_200_OK)
    
class RestaView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno = request.GET.get('num_uno')
        num_dos = request.GET.get('num_dos')
        resta = int(num_uno) -int(num_dos)

        return Response(resta, status = status.HTTP_200_OK)
    
class MultiplicarView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno = request.GET.get('num_uno')
        num_dos = request.GET.get('num_dos')
        multiplicar = int(num_uno) * int(num_dos)
        return Response(multiplicar, status=status.HTTP_200_OK)
    
class DividirView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno = request.GET.get('num_uno')
        num_dos = request.GET.get('num_dos')
        dividir = int(num_uno) / int(num_dos)

        if dividir != 0:
            respuesta = Response(dividir, status=status.HTTP_200_OK)
        elif dividir == 0:
            respuesta = Response(dividir, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
       
        
        
        return respuesta

