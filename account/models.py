from django.db import models
from django.contrib.auth.models import User

from book.models import PrintedBook, AudioBook


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_vip = models.BooleanField(default=False)
    printed_book = models.ManyToManyField(PrintedBook, related_name='payments', blank=True)
    audio_book = models.ManyToManyField(AudioBook, related_name='payments', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username


class PaymentHistory(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='history')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.amount} - {self.payment.user}"
