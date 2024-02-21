from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import News, Footer, About, Services, Employees, SendApplication
from .serializers import NewsSerializers, FooterSerializers, AboutSerializers, ServicesSerializers, EmployeesSerializers, SendApplicationSerializers
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from utils.models import State

# Create your views here.


def lockout_view(request):
    # add any context data here to pass to the template
    context = {
        'message': settings.HOST,
    }
    return render(request, 'lockout.html', context)


class NewsViewSet(ModelViewSet):
    queryset = News.objects.filter(state=State.objects.first())
    serializer_class = NewsSerializers
    http_method_names = ['get', ]
    lookup_field = 'uuid'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FooterViewSet(ModelViewSet):
    queryset = Footer.objects.filter(state=State.objects.first())
    serializer_class = FooterSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AboutViewSet(ModelViewSet):
    queryset = About.objects.filter(state=State.objects.first())
    serializer_class = AboutSerializers
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.filter(state=State.objects.first())
    serializer_class = ServicesSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class EmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.filter(state=State.objects.first())
    serializer_class = EmployeesSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SendApplicationViewSet(ModelViewSet):
    queryset = SendApplication.objects.all()
    serializer_class = SendApplicationSerializers
    http_method_names = ['post', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




