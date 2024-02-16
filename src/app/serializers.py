from rest_framework import serializers
from .models import News, Image, Footer, About, Services, Employees


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'created_at', 'updated_at', 'publisher', 'published_at',)


class ImageSerializers(serializers.ImageField):
    class Meta:
        model = Image
        fields = ('news', 'image', )


class FooterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'image',)


class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('uuid', 'fullname', 'address', 'position', 'image', 'phone', 'email',)
