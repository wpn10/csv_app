from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=255)
    additional_data = models.JSONField(default=dict)

    def __str__(self):
        return self.name

