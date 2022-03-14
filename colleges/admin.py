from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Colleges
from .models import Interview

# Register your models here.
class CollegesAdmin(admin.ModelAdmin):
    pass

class InterviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Interview,InterviewAdmin)
admin.site.register(Colleges,CollegesAdmin)
