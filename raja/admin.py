from django.contrib import admin
from .models import Student,Teacher


# Register your models here.
admin.site.register([Student,Teacher])
