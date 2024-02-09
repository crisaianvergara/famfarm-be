from rest_framework import serializers
from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at']

