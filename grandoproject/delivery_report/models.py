from django.db import models
from manager_client.models import Client


class DeliveryReport(models.Model):
    """ Модель отчета по доставке """

    CLIENT_NAME_CHOICES = [(client.name, client.name) for client in Client.objects.all()]
    DISPATCHER_CHOICES = [
        ('Ксения Майорова', 'Ксения Майорова'),
        ('Мазалов Максим', 'Мазалов Максим'),
        ('Тольев Алексей', 'Тольев Алексей'),
        ('Анна Нуруллова', 'Анна Нуруллова')
    ]

    direction = models.CharField(max_length=128, null=False)
    driver_name = models.CharField(max_length=128, null=False)
    commentary = models.TextField(max_length=256, blank=True, null=True)
    # Список перевозимых поставщиков
    client_list = models.TextField(max_length=256, choices=CLIENT_NAME_CHOICES)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    dispatcher = models.CharField(max_length=128, choices=DISPATCHER_CHOICES)

    def __str__(self):
        return f'Отчет по направлению {self.direction} успешно обновлен'


class EmailReportToClientSuccess(models.Model):
    """
    Модель используется для оповещения клиентов
    при успешной доставке груза
    """

    direction = models.CharField(max_length=128, null=False)
    message = models.TextField(max_length=2048, blank=True, null=True)
    clients = models.ManyToManyField(Client)
    date = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f'Отчет клиентам: "{self.clients}" успешно отправлен'

