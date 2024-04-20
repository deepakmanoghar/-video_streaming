from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'url', 'uploaded_by', 'created_at']
        read_only_fields = ['uploaded_by', 'created_at']