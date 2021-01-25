from django.contrib import admin
from nce.models import Department, Project, Contact


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject', 'message',)




admin.site.register(Department, DepartmentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)