from django.db import models

class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True, help_text="A unique email for each candidate.")
    phone_number = models.CharField(max_length=15, unique=True, help_text="A unique phone number for each candidate.")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Default ordering