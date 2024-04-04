from django.contrib import admin
from ventas.models import VentasApple
from ventas.models import VentasProductos
class VentasAdmin(admin.ModelAdmin):
    list_display = ["month", "value" , "ubication"]

admin.site.register(VentasApple, VentasAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display = ["product_type" , "amount"]
    
admin.site.register(VentasProductos, VentasAdmin)
# Register your models here.
