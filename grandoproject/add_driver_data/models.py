from django.db import models
import os
from django.core.validators import FileExtensionValidator


class UploadDriverData(models.Model):
    """
    Добавление данных водителей
    """
    name = models.CharField(max_length=128, null=False)
    org_name = models.CharField(max_length=128, null=True)
    other_data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    files = models.FileField(blank=True, null=True,
                             upload_to=f'driver_data/',
                             validators=[FileExtensionValidator(allowed_extensions=['zip'])])

    def save(self, *args, **kwargs):
        if self.files and self.name:
            filename = os.path.basename(self.files.name)
            folder_path = os.path.join('driver_data_files', self.name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            self.files.name = os.path.join(folder_path, filename)

        self.name = self.name.lower()
        if self.org_name:
            self.org_name = self.org_name.lower()

        super().save(*args, **kwargs)

    def has_file(self):
        return bool(self.files) and os.path.exists(self.files.path)

    def __str__(self):
        return self.name
