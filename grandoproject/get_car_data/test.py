from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from add_car_data.models import UploadCarData, UploadTrailerData


class GetCarDataTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')


    def test_get_car_data_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('get_car_data:get_car_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_car_data/get_car_data.html')


    def test_download_car_data(self):
        self.client.force_login(self.user)
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        car_data = UploadCarData.objects.create(car_name='test_car', car_scan_doc=file)
        response = self.client.get(reverse('get_car_data:download_car_data', args=[car_data.pk]))
        downloaded_content = b''.join(response.streaming_content)
        self.assertEqual(downloaded_content, file_content)


    def test_get_trailer_data_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('get_car_data:get_trailer_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'get_car_data/get_trailer_data.html')


    def test_download_trailer_data(self):
        self.client.force_login(self.user)
        file_content = b"file content"
        file = SimpleUploadedFile('test_file.zip', file_content)
        trailer_data = UploadCarData.objects.create(car_name='test_trailer', car_scan_doc=file)
        response = self.client.get(reverse('get_car_data:download_trailer_data', args=[trailer_data.pk]))
        downloaded_content = b''.join(response.streaming_content)
        self.assertEqual(downloaded_content, file_content)


    def test_search_car_field(self):
        self.client.force_login(self.user)
        UploadCarData.objects.create(car_number='В244ТК147')
        expected_result = UploadCarData.objects.filter(car_number='В244ТК147')
        response = self.client.get(reverse('get_car_data:search_car_field'), {'q': 'В244ТК147'})
        self.assertEqual(response.status_code, 200)
        actual_result = response.context['car_data']
        # обязательно сравниваем именно квери сеты
        self.assertQuerySetEqual(actual_result, expected_result)


    def test_search_trailer_field(self):
        self.client.force_login(self.user)
        UploadTrailerData.objects.create(trailer_number='АХ4885 48')
        expected_result = UploadTrailerData.objects.filter(trailer_number='АХ4885 48')
        response = self.client.get(reverse('get_car_data:search_trailer_field'), {'q': 'АХ4885 48'})
        self.assertEqual(response.status_code, 200)
        actual_result = response.context['trailer_data']
        # обязательно сравниваем именно квери сеты
        self.assertQuerySetEqual(actual_result, expected_result)



