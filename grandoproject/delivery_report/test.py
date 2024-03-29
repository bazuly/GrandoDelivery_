from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from django.core import mail
from manager_client.models import Client as ClientEmail


class DeliveryReportEmailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_delivery_report_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delivery_report:delivery_report_email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delivery_report/delivery_report_email.html')

    def test_delivery_report_view_post(self):
        self.client.force_login(self.user)
        data = {
            'direction': 'test_direction',
            'message': 'test_message',
            'date': '12.02.2024'
        }
        response = self.client.post(reverse('delivery_report:delivery_report_history'), data)
        self.assertEqual(response.status_code, 200)

    def test_email_sent_successfully(self):
        self.client.force_login(self.user)
        data = {
            'direction': 'Test Direction',
            'message': 'Test Message',
            'date': '2024-02-14',
            'clients': [client.pk for client in ClientEmail.objects.all()]
        }
        response = self.client.post(reverse('delivery_report:delivery_report_email'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), len(data['clients']))
