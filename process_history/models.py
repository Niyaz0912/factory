from django.db import models
from users.models import User


class ProcessHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parameter_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
