from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class CSVData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    domain_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=500, null=True, blank=True)
    integer = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)], null=True, blank=True)

    address = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


def csv_file(instance, filename):
    return '/'.join(['csv_files', str(instance.user.username), filename])


class CSVFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    csv_data = models.ForeignKey(CSVData, on_delete=models.CASCADE, related_name='csvfile')
    file = models.FileField(upload_to=csv_file)

    def __str__(self):
        return self.user.username
