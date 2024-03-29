from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from add_driver_data.models import UploadDriverData


class GetDriverDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_download_driver_data(self):
        self.client.force_login(self.user)
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        driver_data = UploadDriverData.objects.create(name='test_driver', files=file)
        response = self.client.get(reverse('get_driver_data:download_driver_data', args=[driver_data.pk]))
        downloaded_content = b''.join(response.streaming_content)
        self.assertEqual(downloaded_content, file_content)

    def test_search_driver_data(self):
        self.client.force_login(self.user)
        UploadDriverData.objects.create(name='test_driver')
        UploadDriverData.objects.create(org_name='test_org')

        expected_result_name = UploadDriverData.objects.filter(name='test_driver')
        expected_result_org_name = UploadDriverData.objects.filter(org_name='test_org')

        response_name = self.client.get(reverse('get_driver_data:search_driver_data'), {'q': 'test_driver'})
        response_org_name = self.client.get(reverse('get_driver_data:search_driver_data'), {'q': 'test_org'})

        self.assertEqual(response_name.status_code, 200)
        self.assertEqual(response_org_name.status_code, 200)

        actual_result_name = response_name.context['driver_data']
        actual_result_org_name = response_org_name.context['driver_data']

        self.assertQuerySetEqual(actual_result_name, expected_result_name)
        self.assertQuerySetEqual(actual_result_org_name, expected_result_org_name)

