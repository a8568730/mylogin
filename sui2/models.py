from django.db import models

# Create your database models here.
class 使用者表格(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username + self.password 