from django import forms
from .models import (
    Brand, Category, Motherboard, CPU, RAM, PSU, GPU, Case, Storage, Product
)
class ProductFilterForm(forms.Form):
    price_min = forms.DecimalField(required=False, label='Min Price', min_value=0)
    price_max = forms.DecimalField(required=False, label='Max Price', min_value=0)
    rating_min = forms.DecimalField(required=False, label='Min Rating', min_value=0, max_value=5, decimal_places=1)
    rating_max = forms.DecimalField(required=False, label='Max Rating', min_value=0, max_value=5, decimal_places=1)
    
    category = forms.ChoiceField(
        required=False, 
        choices=[('', 'Select a category')] + [(category.name, category.name) for category in Category.objects.all()], 
        label='Category'
    )
    
    brand = forms.ChoiceField(
        required=False, 
        choices=[('', 'Select a brand')] + [(brand.name, brand.name) for brand in Brand.objects.all()], 
        label='Brand'
    )
    
    sort_by = forms.ChoiceField(
        required=False, 
        choices=[
            ('', 'Sort By'),
            ('name', 'Name'),
            ('price', 'Price'),
            ('rating', 'Rating'),
        ], 
        label='Sort By'
    )

# General Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'brand', 'sku', 'name', 'description',
                  'available_quantity', 'price', 'is_discounted', 
                  'discount_price', 'is_featured', 'image_url', 'image', 'rating']


# Motherboard Form
class MotherboardForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Motherboard
        fields = ProductForm.Meta.fields + ['form_factor', 'ram_technology', 'cpu_socket', 'memory_clock_speed']


# CPU Form
class CPUForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = CPU
        fields = ProductForm.Meta.fields + ['cpu_socket', 'cpu_speed', 'secondary_cache',
                                            'cache', 'wattage', 'processor_count', 'cores']


# RAM Form
class RAMForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = RAM
        fields = ProductForm.Meta.fields + ['ram_technology', 'memory_size', 'no_sticks', 'memory_speed']


# PSU Form
class PSUForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = PSU
        fields = ProductForm.Meta.fields + ['form_factor', 'wattage']


# GPU Form
class GPUForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = GPU
        fields = ProductForm.Meta.fields + ['g_ram_technology', 'clock_speed', 'g_ram_size', 'video_interface']


# Case Form
class CaseForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Case
        fields = ProductForm.Meta.fields + ['form_factor', 'has_rgb', 'max_gpu_length',
                                            'max_cpu_cooler_height', 'max_psu_length']


# Storage Form
class StorageForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Storage
        fields = ProductForm.Meta.fields + ['storage_type', 'capacity', 'read_speed', 'write_speed']


# Brand and Category Forms
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'image_url', 'image', 'is_featured']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']