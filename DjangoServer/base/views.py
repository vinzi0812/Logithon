from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.middleware.csrf import get_token
from .models import *
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
import time

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login Successful', 'token': str(AccessToken.for_user(user))}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
class RouteView(APIView):
    def get(self, request):
        routes = Route.objects.all()
        return Response({'message': 'Routes', 'routes': [model_to_dict(route) for route in routes]})
    
    def post(self, request):
        source = request.data.get('source')
        destination = request.data.get('destination').split(',')
        isTransShipment = request.data.get('isTransShipment')
        weight = request.data.get('weight')
        modes_of_transport = request.data.get('modes_of_transport').split(',')
        
        # code integration goes here
        
        return Response({'message': 'Route options', 'routes': []}, status=status.HTTP_200_OK)
    
class RouteChoice(APIView):
    def post(self, request):
        source = request.data.get('source')
        destination = request.data.get('destination')
        mode_of_transport = request.data.get('mode_of_transport')
        cost = request.data.get('cost')
        carbon_emission = request.data.get('carbon_emission')
        duration = request.data.get('duration')
        route = Route(source=source, destination=destination, mode_of_transport=mode_of_transport, cost=cost, carbon_emission=carbon_emission, duration=duration)
        route.save()
        return Response({'message': 'Route saved successfully'}, status=status.HTTP_201_CREATED)

class Cost(APIView):
    def get(self, request):
        #get all routes of past week
        #create a array of dates of past week
        dates = []
        for i in range(7):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes7 = Route.objects.filter(date__in=dates)
        for i in range(14):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes14 = Route.objects.filter(date__in=dates)
        total_cost7, total_cost14 = 0, 0
        for route in routes7:
            total_cost7 += route.cost
        for route in routes14:
            total_cost14 += route.cost
        diff = total_cost14 - total_cost7
        percentage_change = (diff / (total_cost14 - total_cost7)) * 100
        return Response({'message': 'Total cost of all routes', 'total_cost': total_cost7, 'change': percentage_change}, status=status.HTTP_200_OK)     
    
class CarbonEmission(APIView):
    def get(self, request):
        #get all routes of past week
        #create a array of dates of past week
        dates = []
        for i in range(7):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes7 = Route.objects.filter(date__in=dates)
        for i in range(14):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes14 = Route.objects.filter(date__in=dates)
        total_carbon_emission7, total_carbon_emission14 = 0, 0
        for route in routes7:
            total_carbon_emission7 += route.carbon_emission
        for route in routes14:
            total_carbon_emission14 += route.carbon_emission
        diff = total_carbon_emission14 - total_carbon_emission7
        percentage_change = (diff / (total_carbon_emission14 - total_carbon_emission7)) * 100
        return Response({'message': 'Total carbon emission of all routes', 'total_carbon_emission': total_carbon_emission7, 'change': percentage_change}, status=status.HTTP_200_OK)
    
class Duration(APIView):
    def get(self, request):
        #get all routes of past week
        #create a array of dates of past week
        dates = []
        for i in range(7):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes7 = Route.objects.filter(date__in=dates)
        for i in range(14):
            dates.append(time.strftime('%Y-%m-%d', time.localtime(time.time() - i * 86400)))
        routes14 = Route.objects.filter(date__in=dates)
        total_duration7, total_duration14 = 0, 0
        for route in routes7:
            total_duration7 += route.duration
        for route in routes14:
            total_duration14 += route.duration
        average_duration7 = total_duration7 / 7
        average_duration14 = total_duration14 / 14
        diff = average_duration14 - average_duration7
        percentage_change = (diff * 7 / (total_duration14 - total_duration7)) * 100
        return Response({'message': 'Total duration of all routes', 'total_duration': total_duration7, 'change': percentage_change}, status=status.HTTP_200_OK)   