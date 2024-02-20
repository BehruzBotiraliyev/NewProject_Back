from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import State

# Register your models here.


admin.site.site_header = "Project Admin Panel"
admin.site.site_title = "Project Admin Panel"
admin.site.index_title = "Project Admin Panel"


class StateAdmin(TranslationAdmin):
    list_filter = ('title', )
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
    )


admin.site.register(State, StateAdmin)
