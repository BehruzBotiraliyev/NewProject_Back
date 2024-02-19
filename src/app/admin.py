from django.contrib import admin
from .models import News, Image, Footer, About, Services, Employees, EmployeePositions

# Register your models here.

admin.site.site_header = "Project Admin panel"
admin.site.site_title = "Project Admin panel"
admin.site.index_title = "Project Admin panel"


admin.site.register(News)
admin.site.register(Image)
admin.site.register(Footer)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Employees)
admin.site.register(EmployeePositions)


