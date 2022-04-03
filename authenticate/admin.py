from django.contrib import admin
from authenticate.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id_numb', 'first_name', 'last_name', 'email',)
admin.site.register(User,UserAdmin)


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name',)
admin.site.register(Department,DepartmentAdmin)



class FacultyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_per_page = 10 # No of records per page 
admin.site.register(Faculty,FacultyAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_per_page = 10 # No of records per page 
admin.site.register(Country,CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ('code','country', 'name',)
    list_per_page = 10 # No of records per page 
admin.site.register(State,StateAdmin)

class Local_GovernmentAdmin(admin.ModelAdmin):
    list_display = ('pk','state', 'name',)
    list_per_page = 10 # No of records per page 
admin.site.register(Local_Government,Local_GovernmentAdmin)
