from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name