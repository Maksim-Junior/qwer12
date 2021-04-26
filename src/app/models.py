from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=30)
    data = models.JSONField()

    def __str__(self):
        return self.data, self.field
