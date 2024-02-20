from rest_framework import serializers
from django.db.models import Sum
from .models import News, Image, Footer, About, Services, Employees


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'created_at', 'updated_at', 'published_at', 'image', 'views')


class ImageSerializers(serializers.ImageField):
    class Meta:
        model = Image
        fields = ('id', 'image',  'created_at')


class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.get_image_url
        return representation


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('uuid', 'fullname', 'address', 'position', 'image', 'phone', 'email')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.get_image_url()
        return representation
