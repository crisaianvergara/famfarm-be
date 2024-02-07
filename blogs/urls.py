from django.urls import path
from blogs import views


urlpatterns = [
  path('blogs/', views.BlogListView.as_view()),
  path('blogs/<int:pk>', views.BlogDetailView.as_view()),
]