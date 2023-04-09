from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

# Import Generic class
from rest_framework.generics import ListAPIView

# Import Blog app Models
from blog_app.models import BlogPost

# Filter Classes
from blog_app.filters import BlogPostFilter

# Import Blog app Serializers
from blog_app.serializers import BlogListSerializers
from blog_app.serializers import CreateUpdateBlogSerializers
from blog_app.serializers import AuthorBlogDetailSerializer

class AuthorBlogView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.filter(is_active = True)

    serializer_classes = {
        'retrieve' : AuthorBlogDetailSerializer,
        'update': CreateUpdateBlogSerializers,
        'create' : CreateUpdateBlogSerializers
    }

    default_serializer_class = BlogListSerializers

    # Filter Classes
    serializer_class = BlogListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = BlogPostFilter

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_active=True, author=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    # Only author of the blog can update the blog post
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    

    # Overwride the destroy method for soft delete, this method makes is_active=False
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != request.user:
            return Response({'error': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



    
       