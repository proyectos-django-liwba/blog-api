
from django.contrib import admin
from django.urls import path
# importamos la vista creada en la app posts
from posts.views import HelloWordld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', HelloWordld.as_view())
]

# '' es la ruta raiz
# indicamos que es una vista .as_view()
#  deben terminar con un slash /, las que tienen un nombre