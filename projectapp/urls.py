from django.urls import path
from .views import video_list, video_detail

urlpatterns = [
    path('api/videos/', video_list, name='video_list'),
    path('api/videos/<int:pk>/', video_detail, name='video_detail'),
]