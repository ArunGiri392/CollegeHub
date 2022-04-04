from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Colleges,Essays


# Register your models here.
class CollegesAdmin(admin.ModelAdmin):
    pass

class EssaysAdmin(admin.ModelAdmin):
    pass


admin.site.register(Colleges,CollegesAdmin)
admin.site.register(Essays,EssaysAdmin)
