from rest_framework.serializers import ModelSerializer
from account.models import UserProfile, Payment, PaymentHistory


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentHistorySerializer(ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'
