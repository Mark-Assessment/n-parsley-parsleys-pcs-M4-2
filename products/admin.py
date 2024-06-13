from django.contrib import admin

# Register your models here.
from .models import Category, Brand, CPU, GPU, PSU, RAM, Motherboard

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(PSU)
admin.site.register(RAM)
admin.site.register(Motherboard)
