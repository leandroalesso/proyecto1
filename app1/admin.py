from django.contrib import admin
from app1.models import *

# Register your models here.

class Clase1Admin(admin.ModelAdmin):
    list_display=('titulo',)
    search_fields=('titulo',)
    fieldsets=(
        (u'Titulacion', {'fields':('titulo',)}),
    )

admin.site.register(Clase1, Clase1Admin)
