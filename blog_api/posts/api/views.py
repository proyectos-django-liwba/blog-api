# agregar el response
from rest_framework import status
from rest_framework.response import Response
# agregar la clase APIView
#from rest_framework.views import APIView
# agregar viewsets
#from rest_framework.viewsets import ViewSet
# agregar modelviewset
from rest_framework.viewsets import ModelViewSet
# hacer uso de ORM de django para obtener los datos de BD
from posts.models import Post
# validar los datos antes de crear el objeto Post
from rest_framework.exceptions import ValidationError
# serializar los objetos
from posts.api.serializers import PostSerializer
# permisos de acceso
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly


# ModelViewSet

class PostModelViewSet(ModelViewSet):
    # se puede agregar 1 o mas permisos
    permission_classes = [IsAdminOrReadOnly]
    # agregar el serializador
    serializer_class = PostSerializer
    # agregar todas las operaciones GET, POST, PUT, DELETE
    queryset = Post.objects.all()
    # definir las operaciones que se pueden realizar
    http_method_names = ['get', 'post', 'put', 'delete']





# ViewSet
""" class PostViewSet(ViewSet):
    
    # obtener todos los posts mediante el ORM de django
    def list(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    # obtener un post por id
    def retrieve(self, request, pk=int):
        try:
            #post = Post.objects.filter(id=pk).first()
            post = PostSerializer(Post.objects.get(pk=pk))
            
            return Response(status=status.HTTP_200_OK, data=post.data)

        except Exception as e:
            # Manejar otros errores
            return Response(data={"error":"Post no encontrado.", "description": str(e)}, status=status.HTTP_404_NOT_FOUND)


    # agregar el metodo post
    def create(self, request):
        try:
            serializer = PostSerializer(data=request.data)
            # validar los datos
            serializer.is_valid(raise_exception=True)

            # crear el objeto
            serializer.save()
            
            return Response(status=status.HTTP_201_CREATED, data={"message":"Post creado correctamente", "data":serializer.data})

        except ValidationError as e:
            # Manejar errores de validación
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Manejar otros errores
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 """

# APIView
""" 
class PostApiView(APIView):
    def get(self, request):
        # obtener todos los posts mediante el ORM de django
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    # agregar el metodo post
    def post(self, request):
        try:
            serializer = PostSerializer(data=request.data)
            # validar los datos
            serializer.is_valid(raise_exception=True)

            # crear el objeto
            serializer.save()
            
            return Response(status=status.HTTP_201_CREATED, data={"message":"Post creado correctamente", "data":serializer.data})

        except ValidationError as e:
            # Manejar errores de validación
            return Response({'error': e.detail}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Manejar otros errores
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""