from django.contrib import admin
from .models import House,Flat,People

class FlatInline(admin.TabularInline):
    model = Flat
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [FlatInline]

admin.site.register(House,HouseAdmin)
admin.site.register(Flat)
admin.site.register(People)
