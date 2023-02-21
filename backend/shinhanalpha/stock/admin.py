from django.contrib import admin
from .models import Stock, Cart
# Register your models here.
@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class StockAdmin(admin.ModelAdmin):
    pass