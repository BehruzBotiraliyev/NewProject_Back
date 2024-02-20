from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import News, Footer, About, Services, Employees
from .serializers import NewsSerializers, FooterSerializers, AboutSerializers, ServicesSerializers, EmployeesSerializers

# Create your views here.


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    http_method_names = ['get', ]
    lookup_field = 'uuid'

    def retrieve(self, request, *args, **kwargs):
        instanse = self.get_queryset()
        news = instanse.first()
        news.increase_views()
        news.save()
        return self.super().retrieve(self, request, *args, **kwargs)




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





