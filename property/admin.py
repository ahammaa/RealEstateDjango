from django.contrib import admin

# Register your models here.
from .models import *

from .forms import *

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display=["__str__","type"]
    class Meta:
        model=PropertyType

class PropertyPlaceAdmin(admin.ModelAdmin):
    list_display=["__str__","place"]
    class Meta:
        model=PropertyPlace

class PropertyFloorAdmin(admin.ModelAdmin):
    list_display=["__str__","floor"]
    class Meta:
        model=PropertyFloor


class SellerAdmin(admin.ModelAdmin):
    list_display=["__str__","name","phone","email","agent"]
    class Meta:
        model=Seller

class PropertyAdmin(admin.ModelAdmin):
    list_display=["__str__","type","price","date"]
    #form = PropertyForm
    class Meta:
        model=Property
    def ptype_type(self):
        return self.type.type

class ContactAdmin(admin.ModelAdmin):
    list_display=["__str__","date","type","subject","checked","display"]
#    form = ContactForm
    class Meta:
        model=Contact
    #class Meta:
    #    model=Property

admin.site.register(Seller,SellerAdmin)
admin.site.register(PropertyType,PropertyTypeAdmin)
admin.site.register(PropertyPlace,PropertyPlaceAdmin)
admin.site.register(PropertyFloor,PropertyFloorAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Contact,ContactAdmin)
