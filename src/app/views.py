from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import News, Footer, About, Services, Employees
from .serializers import NewsSerializers, FooterSerializers, AboutSerializers, ServicesSerializers, EmployeesSerializers

# Create your views here.


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    http_method_names = ['get', ]


class FooterViewSet(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializers
    http_method_names = ['get', ]


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializers
    http_method_names = ['get', ]


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    http_method_names = ['get', ]


class EmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializers
    http_method_names = ['get', ]





