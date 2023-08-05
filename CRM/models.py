from django.db import models

# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=120)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    """
    : String :  Waiting his order/ bought/ didn't pay / completed / etc.
    """
    status = models.CharField(max_length=20, blank=True, null=True)
    """
    : String : Where did he found you / special information to know about him/her, etc.
    """
    summary = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return f"Customer_name: '{self.first_name} {self.last_name}', Email: '{self.email}', status: '{self.status}'"
    
    def __dict__(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'status': self.status,
            'summary': self.summary,
        }