from rest_framework.routers import DefaultRouter
#from posts.api.views import PostViewSet
from posts.api.views import PostModelViewSet

#definir el router de la app
router_post = DefaultRouter()

#registrar rutas
#router_post.register(prefix='posts', basename='posts', viewset=PostViewSet)
router_post.register(prefix='posts', basename='posts', viewset=PostModelViewSet)