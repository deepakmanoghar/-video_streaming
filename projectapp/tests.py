from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Video

class VideoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'test_user',
            'password': 'test_password'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)
        self.video_data = {
            'name': 'Test Video',
            'url': 'http://example.com/video.mp4'
        }
        self.video = Video.objects.create(**self.video_data)

    def test_create_video(self):
        url = reverse('video_list')
        response = self.client.post(url, self.video_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 2)

    def test_get_video_list(self):
        url = reverse('video_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.video.name)

    def test_get_video_detail(self):
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.video.name)

    def test_update_video(self):
        updated_name = 'Updated Video Name'
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        data = {'name': updated_name}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.video.refresh_from_db()
        self.assertEqual(self.video.name, updated_name)

    def test_delete_video(self):
        url = reverse('video_detail', kwargs={'pk': self.video.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Video.objects.count(), 0)