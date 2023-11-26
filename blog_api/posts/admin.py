from django.contrib import admin

# importar modelos de la app
from posts.models import Post

# agregar un decorador para registrar el modelo
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # campos que se van a mostrar en el admin
    list_display = ('title', 'description', 'views', 'created_at')