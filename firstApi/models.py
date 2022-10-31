from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




