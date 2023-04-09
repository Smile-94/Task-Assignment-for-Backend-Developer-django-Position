from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# Import Blog app Models
from blog_app.models import BlogPost

# Import Blog app Serializers
from blog_app.serializers import BlogListSerializers
from blog_app.serializers import CreateUpdateBlogSerializers
from blog_app.serializers import AuthorBlogDetailSerializer

class AuthorBlogView(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.filter(is_active = True)
    serializer_classes = {
        'retrieve' : AuthorBlogDetailSerializer,
        'update': CreateUpdateBlogSerializers,
        'create' : CreateUpdateBlogSerializers
    }
    default_serializer_class = BlogListSerializers
    lookup_field = 'id'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    

    # Overwride the destroy method for soft delete, this method makes is_active=False
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
        return Response({'message':'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
       