from django.contrib import admin
from .models import CustomUser, Empresa

admin.site.register(CustomUser)
admin.site.register(Empresa)
