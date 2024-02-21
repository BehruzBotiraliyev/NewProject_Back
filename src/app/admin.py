from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, Image, Footer, About, Services, Employees, EmployeePositions, ServiceType, SendApplication

# Register your models here.

admin.site.site_header = "Project Admin panel"
admin.site.site_title = "Project Admin panel"
admin.site.index_title = "Project Admin panel"


class NewsAdmin(TranslationAdmin):
    list_filter = ('title', 'state', 'created_at')
    search_fields = ('title', 'content')
    list_per_page = 20
    list_display = ('title', 'state', 'created_at')

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Rasm', {'fields': ('image',)}),
        ('Chop etilgan vaqti', {'fields': ('published_at',)}),
        ('Xolati', {'fields': ('state',)}),
    )


class AboutAdmin(TranslationAdmin):
    list_filter = ('title', 'state', 'created_at')
    search_fields = ('title', 'content')
    list_per_page = 20
    list_display = ('title', 'state')

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Rasm', {'fields': ('image',)}),
        ('State', {'fields': ('state',)}),
    )


class EmployeesAdmin(TranslationAdmin):
    list_filter = ('fullname', 'state', 'position')
    search_fields = ('fullname', 'address')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('fullname_uz', 'address_uz',)}),
        ('Inglizcha', {'fields': ('fullname_en', 'address_en',)}),
        ('Ruscha', {'fields': ('fullname_ru', 'address_ru')}),
        ('Lavozimi', {'fields':  ('position',)}),
        ('Rasm', {'fields': ('image',)}),
        ('Telefon raqamlar', {'fields': ('phone',)}),
        ('Email', {'fields': ('email',)}),
        ('State', {'fields': ('state',)}),
    )


class EmployeePositionsAdmin(TranslationAdmin):
    list_filter = ('title',)
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
    )


class ServicesAdmin(TranslationAdmin):
    list_filter = ('title', 'state', 'service_type')
    search_fields = ('title', 'content')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'content_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'content_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'content_ru',)}),
        ('Xizmat turi', {'fields': ('service_type',)}),
        ('Ikonka', {'fields': ('icon',)}),
        ('Xolati', {'fields': ('state',)}),
    )


class ServiceTypeAdmin(TranslationAdmin):
    list_filter = ('title',)
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
    )


admin.site.register(News, NewsAdmin)
admin.site.register(Image)
admin.site.register(Footer)
admin.site.register(About, AboutAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(EmployeePositions, EmployeePositionsAdmin)
admin.site.register(SendApplication)
