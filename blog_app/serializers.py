from rest_framework import serializers
import re

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
    
    summary = serializers.SerializerMethodField()
    num_words = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ( 'id' ,'title','author','published_date','category','content','summary','num_words')
    
    def get_summary(self, obj):
        return obj.generate_summary()

    def get_num_words(self, obj):
        words = re.findall(r'\w+', obj.content)
        return len(words)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author']=UserDetaillSerializers(instance=instance.author).data
        return data


class CreateUpdateBlogSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('title','status','category','content')


class AuthorBlogDetailSerializer(serializers.ModelSerializer):

    summary = serializers.SerializerMethodField()
    num_words = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = '__all__'

    def get_summary(self, obj):
        return obj.generate_summary()

    def get_num_words(self, obj):
        words = re.findall(r'\w+', obj.content)
        return len(words)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author']=UserDetaillSerializers(instance=instance.author).data
        return data