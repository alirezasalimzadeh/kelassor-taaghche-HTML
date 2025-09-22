from django.contrib import admin

from account.models import UserProfile, Payment, PaymentHistory

admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(PaymentHistory)
