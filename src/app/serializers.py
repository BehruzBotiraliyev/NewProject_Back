from rest_framework import serializers
from .models import News, Image, Footer, About, Services, Employees, ServiceType, EmployeePositions, SendApplication


class ImageSerializers(serializers.ImageField):
    class Meta:
        model = Image
        fields = ('id', 'image',  'created_at')


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'created_at', 'updated_at', 'published_at', 'image', 'views')


class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('id', 'email', 'phone', 'address', 'logo', 'facebook', 'instagram', 'telegram', 'youtube',
                  'created_at', 'updated_at')


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image')


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('title', 'content', 'icon', 'service_type', 'created_at')


class ServiceTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'attr')


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('uuid', 'fullname', 'address', 'position', 'image', 'phone', 'email')


class EmployeePositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeePositions
        fields = '__all__'


class SendApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = SendApplication
        fields = '__all__'
