from django.contrib import admin
#agregar un alias para evitar conflictos por el nombre
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
   # pass # no hace nada, solo hereda de BaseUserAdmin
    fieldsets = (
        (None, {'fields': ('email', 'password')}), # None es el titulo
        ('Informacion Personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Informacion de contacto', {'fields': ('web_site', 'cellphone')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
# los nombres de los campos deben ser los mismos que en el modelo y bd