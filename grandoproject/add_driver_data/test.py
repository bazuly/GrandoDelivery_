from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class AddDriverDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_add_driver_data_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_driver_data:add_driver_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_driver_data/add_driver_data.html')

    def test_add_driver_data_view_post(self):
        self.client.force_login(self.user)
        data = {
            "name": 'test_driver',
            "org_name": 'test_org',
            "other_data": 'test_name \n'
                          'test_phone_number \n'
                          'test_passport \n'
                          'test_driver_license'
        }
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        data['files'] = file
        response = self.client.post(reverse('add_driver_data:add_driver_data'), data, follow=True)
        self.assertEqual(response.status_code, 200)

