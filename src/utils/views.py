from rest_framework.viewsets import ModelViewSet
from .serializers import StateSerializers
from .models import State
from rest_framework.response import Response

# Create your views here.


class StateView(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializers
    http_method_names = ['get']

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

