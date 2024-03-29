from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from manager_client.models import Client as ClientModel


class GetManagerClientTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_get_client_data_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('manager_client:get_client_data'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/list_client.html')

    def test_search_client(self):
        self.client.force_login(self.user)
        ClientModel.objects.create(name='test_client')
        expected_result = ClientModel.objects.filter(name='test_client')
        response = self.client.get(reverse('manager_client:search_client'), {'q': 'test_client'})
        self.assertEqual(response.status_code, 200)
        actual_result = response.context['client_data']
        self.assertQuerySetEqual(actual_result, expected_result)