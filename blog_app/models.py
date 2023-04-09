from django.db import models
from django.utils import timezone
import datetime
import re

# Import Truncator to generate Summery
from django.utils.text import Truncator

# Import django defaults Models
from django.contrib.auth import get_user_model
User = get_user_model() #User Model

# Create your models here.
class BlogPost(models.Model):
    # Choices for the status of the blog post
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    # Choices for the category of the blog post
    CATEGORY_CHOICES = (
        ('tech', 'Technology'),
        ('lifestyle', 'Lifestyle'),
        ('politics', 'Politics'),
        ('entertainment', 'Entertainment'),
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('business', 'Business'),
        ('education', 'Education'),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(default=True) # This fields used to soft-delete the blog post

    # This function wll save the published date when blogpost status is published
    def publish(self):
        if self.status == 'published':
            self.published_date = datetime.now()
            self.save()
    
    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_date:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)
    
    def generate_summary(self):
        # Count words in content
        words = re.findall(r'\w+', self.content)
        num_words = len(words)
        
        # Split content into sentences
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', self.content)
        
        # Select first five sentences of the blog post as summary
        summary = ' '.join(sentences[:5])
        
        # Add '...' if summary of blog post is less than content
        if len(summary.split()) < num_words:
            summary += '...'
        
        return summary

    def __str__(self):
        return self.title[:30]