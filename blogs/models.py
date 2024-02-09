from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  author = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return self.title