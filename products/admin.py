from django.contrib import admin

# Register your models here.
from .models import Category, Brand, CPU, GPU, PSU, RAM, Motherboard, CPUSocket, RAMTechnology, FormFactor, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(PSU)
admin.site.register(RAM)
admin.site.register(Motherboard)
admin.site.register(CPUSocket)
admin.site.register(RAMTechnology)
admin.site.register(FormFactor)
admin.site.register(Product)
