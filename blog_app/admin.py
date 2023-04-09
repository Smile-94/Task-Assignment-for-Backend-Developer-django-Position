from django.contrib import admin

# Blog app Models
from blog_app.models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date','status','category')
    search_fields = ('title','author','category')
    list_filter = ('status','category')
    raw_id_fields = ('author',)
    list_per_page = 50
