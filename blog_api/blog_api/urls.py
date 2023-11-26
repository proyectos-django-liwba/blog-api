# importamos la vista creada en la app posts
#from posts.views import HelloWordld

from django.contrib import admin
from django.urls import path, include
#from posts.api.views import PostApiView
#from posts.api.views import PostViewSet
from posts.api.router import router_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls)),
    #path('api/posts/', PostApiView.as_view())
    #path('posts/', HelloWordld.as_view())
]

# '' es la ruta raiz
# indicamos que es una vista .as_view()
#  deben terminar con un slash /, las que tienen un nombre