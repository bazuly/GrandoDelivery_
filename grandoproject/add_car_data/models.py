from django.db import models
import os
from django.core.validators import FileExtensionValidator


class UploadCarData(models.Model):
    """Добавление данных транспортых средств"""

    car_name = models.CharField(max_length=50, null=True, blank=True)
    car_number = models.CharField(max_length=48, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    TONNAGE_CHOICES = [
        (1.5, '1.5 тонны'),
        (2, '2 тонны'),
        (3, '3 тонны'),
        (5, '5 тонн'),
        (7, "7 тонн"),
        (10, '10 тонн'),
        (20, '20 тонн'),
    ]

    tonnage = models.FloatField(choices=TONNAGE_CHOICES, blank=True, null=True)

    # кол-во паллет
    capacity = models.IntegerField(null=True)

    car_scan_doc = models.FileField(blank=True, null=True,
                                    upload_to='car_data/',
                                    validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    def save(self, *args, **kwargs):
        if self.car_scan_doc and self.car_name:
            filename = os.path.basename(self.car_scan_doc.name)
            folder_path = os.path.join('car_data_files', self.car_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            self.car_scan_doc.name = os.path.join(folder_path, filename)
        
        super().save(*args, **kwargs)

    def has_file(self):
        return bool(self.car_scan_doc) and os.path.exists(self.car_scan_doc.path)

    def __str__(self):
        return self.car_number


class UploadTrailerData(models.Model):
    """Добавление данных полуприцепов"""

    trailer_name = models.CharField(null=True,
                                    max_length=48,
                                    blank=True)

    trailer_number = models.CharField(max_length=48,
                                      null=True,
                                      blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    trailer_scan_doc = models.FileField(blank=True, null=True,
                                        upload_to='trailer_data/',
                                        validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    def has_file(self):
        return bool(self.trailer_scan_doc) and os.path.exists(self.trailer_scan_doc.path)

    def save(self, *args, **kwargs):
        if self.trailer_scan_doc and self.trailer_name:
            filename = os.path.basename(self.trailer_scan_doc.name)
            folder_path = os.path.join('trailer_data_files', self.trailer_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            self.trailer_scan_doc.name = os.path.join(folder_path, filename)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.trailer_number
