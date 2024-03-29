from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class AddCarDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_add_car_data_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_car_data:add_car_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_car_data/add_car_data.html')

    def test_add_car_data_view_post(self):
        self.client.force_login(self.user)
        data = {
            'car_name': 'test_car',
            'car_number': 'А886ВУ147',
            'tonnage': 20,
            'capacity': 33,
        }
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        data['car_scan_doc'] = file
        response = self.client.post(reverse('add_car_data:add_car_data'), data, follow=True)
        self.assertEqual(response.status_code, 200)


class AddTrailerDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_add_car_data_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_car_data:add_trailer_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_car_data/add_trailer_data.html')

    def test_add_trailer_data_view_post(self):
        self.client.force_login(self.user)
        data = {
            'trailer_name': 'test_trailer',
            'trailer_number': 'АН9988 47',
        }
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        data['trailer_scan_doc'] = file
        response = self.client.post(reverse('add_car_data:add_trailer_data'), data, follow=True)
        self.assertEqual(response.status_code, 200)
