from django.db import models


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=250, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_year = models.DateField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=True)
