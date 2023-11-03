from django.contrib import admin
from .models import ProductDetails, Img

# Register your models here.
# admin.site.register(ProductDetails)

class faqinline(admin.StackedInline):
    model = Img
    extra = 0

class serviceadmin(admin.ModelAdmin):
    inlines = [faqinline]

admin.site.register(ProductDetails, serviceadmin)

admin.site.register(Img)