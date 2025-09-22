from django.shortcuts import render
from rest_framework import generics
from account.models import UserProfile, Payment, PaymentHistory
from account.serializer import ProfileSerializer, PaymentSerializer, PaymentHistorySerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PaymentHistory.objects.all()
    serializer_class = PaymentHistorySerializer


class PaymentHistoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PaymentHistory.objects.all()
    serializer_class = PaymentHistorySerializer
