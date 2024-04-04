from django.db import models
import re


class Manager(models.Model):
    """ Manager Model """

    name = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        if self.manager is not None:
            self.manager = self.manager.lower()
        else:
            self.manager = 'Не назначен'

    def __str__(self):
        return self.name


class Client(models.Model):
    """Модель клиентов/поставщиков"""

    name = models.CharField(max_length=128, null=False)
    contacts = models.TextField(max_length=700)
    manager = models.ForeignKey(Manager, max_length=128, on_delete=models.SET_NULL, null=True, blank=True)
    main_email = models.CharField(max_length=1000, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()

        if self.main_email:
            emails = re.findall(r'[\w\.-]+@[\w\.-]+', self.main_email)
            self.main_email = ','.join(emails)

        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    