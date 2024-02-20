from rest_framework import serializers
from django.db.models import Sum
from .models import News, Image, Footer, About, Services, Employees


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('uuid', 'title', 'content', 'created_at', 'updated_at', 'published_at', 'image', 'images_count',
                  'views',)

    # def to_representation(self, instance):
        # representation = super().to_representation(instance)
        # print(Image.objects.filter(news=instance))
        # print(ImageSerializers(Image.objects.filter(news=instance), many=True))
        # representation['image'] = ImageSerializers(Image.objects.filter(news=instance), many=True).data
        # representation['images_count'] = Image.objects.filter(news=instance).count()
        # return representation


class ImageSerializers(serializers.ImageField):
    class Meta:
        model = Image
        fields = ('image',  'created_at', 'image_count',)


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

