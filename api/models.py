from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255, null=True)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
