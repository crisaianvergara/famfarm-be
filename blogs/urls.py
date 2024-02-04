from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogs import views


urlpatterns = [
  path('blogs/', views.BlogListView.as_view()),
  path('blogs/<int:pk>', views.BlogDetailView.as_view()),
]