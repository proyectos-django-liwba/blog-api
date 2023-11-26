# importamos la vista creada en la app posts
#from posts.views import HelloWordld

from django.contrib import admin
from django.urls import path, include
#from posts.api.views import PostApiView
#from posts.api.views import PostViewSet
from posts.api.router import router_post
# importaciones de la libreria drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# definir el schema
schema_view = get_schema_view(
   openapi.Info(
      title="Documentacion Blog API",
      default_version='v1',
      description="Description endpoint API Blog",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls)),
    # agregar la ruta de la documentacion
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('api/posts/', PostApiView.as_view())
    #path('posts/', HelloWordld.as_view())
]

# '' es la ruta raiz
# indicamos que es una vista .as_view()
#  deben terminar con un slash /, las que tienen un nombre