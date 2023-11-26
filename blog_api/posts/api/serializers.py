from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("id",'title', 'description', 'views', 'created_at')
        
        def validate(self, data):
            errors = {}

            # Validación personalizada para el campo 'title'
            title = data.get('title')
            if not title:
                errors['title'] = 'Este campo es obligatorio.'

            # Validación personalizada para el campo 'description'
            description = data.get('description')
            if not description:
                errors['description'] = 'Este campo es obligatorio.'

            if errors:
                raise serializers.ValidationError(errors)

            return data
