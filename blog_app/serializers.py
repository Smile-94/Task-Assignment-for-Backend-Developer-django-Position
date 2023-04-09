from rest_framework import serializers

# Import django defaults models
from django.contrib.auth import get_user_model

# Import Blog app Models
from blog_app.models import BlogPost

User=get_user_model()

class UserDetaillSerializers(serializers.ModelSerializer):
   class Meta:
    model=User
    fields=('first_name','last_name')

class BlogListSerializers(serializers.ModelSerializer):
  
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'author', 'published_date', 'category')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author']=UserDetaillSerializers(instance=instance.author).data
        return data 
        


class BlogDetailsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = BlogPost
        fields = ( 'id' ,'title','author','published_date','category','content')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author']=UserDetaillSerializers(instance=instance.author).data
        return data


class CreateUpdateBlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('title','status','category','content')


class AuthorBlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author']=UserDetaillSerializers(instance=instance.author).data
        return data