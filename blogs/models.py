from django.db import models

class Blogs(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  author = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  class Meta:
    ordering:['updated_at']