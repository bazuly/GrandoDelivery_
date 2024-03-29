from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    JOB_TITLE_CHOICES = [
        ('Диспетчер-логист', 'Диспетчер-логист'),
        ('Специалист по маршрутизации', 'Специалист по маршрутизации'),
        ('Менеджер по сопровождению клиентов', 'Менеджер по сопровождению клиентов'),
        ('Менеджер по логистике', 'Менеджер по логистике'),
        ('Специалист отдела логистики', 'Специалист отдела логистики'),
        ('Директор транспортного отдела', 'Директор транспортного отдела')

    ]
    job_title = models.CharField(blank=True, null=True, verbose_name='Должность',
                                 max_length=128, choices=JOB_TITLE_CHOICES)
    photo = models.ImageField(blank=True, null=True, verbose_name='Фото профиля', upload_to='users/%Y/%m/%d/')
