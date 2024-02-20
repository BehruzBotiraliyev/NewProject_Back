from rest_framework.viewsets import ModelViewSet
from .models import News, Footer, About, Services, Employees
from .serializers import NewsSerializers, FooterSerializers, AboutSerializers, ServicesSerializers, EmployeesSerializers
from rest_framework.response import Response

from utils.models import State

# Create your views here.


class NewsViewSet(ModelViewSet):
    queryset = News.objects.filter(state=State.objects.last())
    serializer_class = NewsSerializers
    http_method_names = ['get', ]
    lookup_field = 'uuid'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.increase_views()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FooterViewSet(ModelViewSet):
    queryset = Footer.objects.filter(state=State.objects.last())
    serializer_class = FooterSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AboutViewSet(ModelViewSet):
    queryset = About.objects.filter(state=State.objects.last())
    serializer_class = AboutSerializers
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ServicesViewSet(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers
    http_method_names = ['get', ]


class EmployeesViewSet(ModelViewSet):
    queryset = Employees.objects.filter(state=State.objects.last())
    serializer_class = EmployeesSerializers
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





