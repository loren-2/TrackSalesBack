from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('backoffice', 'Backoffice'), ('salesman','Salesman')])

    def __str__(self):
        return self.username


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=50, choices=[('restaurant', 'Restaurant'), ('shop', 'Shop'), ('supermarket', 'Supermarket')])
    address = models.CharField(max_length=200)
    po_box = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name


class Task(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    task_type = models.CharField(max_length=50, choices=[('email', 'Email'),('visit', 'Visit'),('call', 'Call'),
                                                         ('message', 'Message')])
    due_date = models.DateField()
    task_status = models.CharField(max_length=50, choices=[('pending','Pending'), ('in progress', 'In Progress'), ('completed', 'Completed')])
    result = models.TextField(null=True)
    done_date = models.DateField(null=True)

    def __str__(self):
        return self.title
